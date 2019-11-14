# The biggest selling point of inheritance is that we avoid code duplication and it allows us to reuse code.

# However to much from a good thing is a bad thing, to much inheritance in your classes can lead to:

# 1. Increased complexity
# 2. various sorts of unexpected behaviour

# To prove my 2nd point lets do an example:


class Animal:

    def eat(self):
        print('eating...')


class Bird(Animal):

    def fly(self):
        print('flying...')


class Chicken(Bird):

    pass  # A class needs at least one statement.


# Now we can all agree that a bird is an animal and that a chicken is an evil bird.
# But a bird can fly, the chicken can't.

# Still due to inheritance the following is possible:

evil_chick = Chicken()
evil_chick.fly()  # Impossible, luckily for us! [dont ever trust chickens, they have a hidden agenda...]

# Link of proof: https://www.youtube.com/watch?v=z8pknnncODo
