# There are times in programming where we want full control over our attributes.

# In this example we create a Product class,
# its important that when we create an instance of this class our price cant be negative:


class Product:

    def __init__(self, price):
        self.__price = price
        # self.set_price(price)  # This implementation works, but is not Pythonic! [correct way is on line ]

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError('Price cannot be negative!')
        self.__price = value

    @classmethod
    def zero(cls):
        return Product(0)

    price = property(get_price, set_price)


# Lets create a product with a positive price:

product_pos = Product(42)
print(product_pos.price)  # Print the result

# Now we will try the same but with a negative price:

product_pos = Product.zero()
product_pos.price = 10
print(product_pos.price)  # Will throw an exception because of negative price


# Now let us make another class to show how to deal with this in the correct way, and securing our constructor as well:
# This approach lets us use name as a real property of the class.

# TODO fix link to class where it's explained:
# Under the hood implementations will be explained in another class:

class Human:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    # You could even drop this setter if you want a read only property meaning:

    # After initialising an object of this class,
    # you will no longer be able to change it using: elliot.name = 'Diff name' syntax [If tried => AttributeError].
    @name.setter
    def name(self, name):
        if name == '':
            raise ValueError('A name can not be empty!')
        self.__name = name

    def __str__(self):
        return self.__name


# Create an instance to play with:

elliot = Human('Elliot')
# elliot = Human('')  # Uncomment to see exception

# We can use this like a regular attribute:
print(f"Name of the human: {elliot.name}")
