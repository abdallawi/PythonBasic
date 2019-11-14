# In this class we're going to take a look at method overwriting, this can be useful in allot of ways.
# We have a constructor in the Animal class, this constructor will be inherited by every subclass,
# Unless we overwrite it.

# FYI:

# Animal: Parent, Base class
# Mammal: Child, Sub class
# Animal: Child, Sub class


class Animal:

    def __init__(self):
        print('Animal constructor executed')
        self.age = 10

    def eat(self):
        return 'Eating...'

    def __str__(self):
        return f"Animal is {self.age} years old"


class Mammal(Animal):  # To inherit we can use this syntax

    def __init__(self):
        super().__init__()
        print('Mammal constructor executed')
        self.weight = 2

    def walk(self):
        return 'Walking...'


class Fish(Animal):  # To inherit we can use this syntax

    def swim(self):
        return 'Swimming...'


# We created some instances to play with:

animal = Animal()
mammal = Mammal()  # This line of code will throw an AttributeError when we don't do the super call like seen on line 28
fish = Fish()

# Because the constructor of the base class is executed, we still have have its attribute age value set to 10,
# we can still change that value like so:

mammal.age = 4

# Printout of our instances:

print()  # for cleaner printout
print(animal)
print(f"{mammal}, and weighs: {mammal.weight} kg.")
print(fish)

# In recap:

# Method overwriting means replacing or extending a method defined in the Base class.
# We extended the constructor in this example. [which is of course a special method ;)]
