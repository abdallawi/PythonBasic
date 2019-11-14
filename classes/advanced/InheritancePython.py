# Makes sense:

new_line = '\n'

# As you build various classes, you can sometimes spot duplicate features or functions in common.
# Dont believe me, well lets do an example then:


class MammalDupl:

    # Duplicate
    def eat(self):
        print('Eating...')

    def walk(self):
        print('Walking...')


class FishDupl:

    # Duplicate
    def eat(self):
        print('Eating...')

    def swim(self):
        print('Swimming...')

# The biggest problem here is:

# In case multiple classes would be written and we want to change the implementation of the eat method,
# We need to go in to all classes and manually change it; This makes the risk of forgetting it somewhere to big!

# We can fix our problem in 2 ways: Inheritance or Compositions.

# We will use inheritance in this example:

# Animal: Parent, Base class
# Mammal: Child, Sub class
# Animal: Child, Sub class


class Animal:

    # We can also make an attribute that will be inherited in all sub classes:
    def __init__(self):
        self.age = 0

    # We can use these methods[eat, __str__] with all classes that inherit from the Animal class
    # This can be seen from the code written lines 85 till 94.

    def eat(self):
        return 'Eating...'

    def __str__(self):
        return f"Animal is {self.age} years old"


class Mammal(Animal):  # To inherit we can use this syntax

    def walk(self):
        return 'Walking...'


class Fish(Animal):  # To inherit we can use this syntax

    def swim(self):
        return 'Swimming...'


# To test it we create some objects/instances to play around with:

animal = Animal()
mammal = Mammal()
fish = Fish()

# Creating some variables to avoid overenthusiastic function calling:

type_object = type(object())
type_animal = type(animal)
type_mammal = type(mammal)
type_fish = type(fish)

msg_instance_of = 'is an instance of'
msg_subclass_of = 'is a subclass of'

# We can change our shared attribute age:

animal.age = 4
mammal.age = 2
fish.age = 0


# Lets use their methods and see inheritance in action:

print(f"{type_animal} eat: {animal.eat()}")
print(animal, new_line)

print(f"{type_mammal} eat: {mammal.eat()}")
print(f"{type_mammal} walk: {mammal.walk()}")
print(mammal, new_line)

print(f"{type_fish} eat: {fish.eat()}")
print(f"{type_fish} swim: {fish.swim()}")
print(fish, new_line)

# Every class in Python actually inherits from the object class,
# You can test this in the following way:

print(f'{"animal"} {msg_instance_of} {type_object}: {isinstance(animal, object)}')
print(f'{"mammal"} {msg_instance_of} {type_object}: {isinstance(mammal, object)}')
print(f'{"fish"} {msg_instance_of} {type_object}: {isinstance(fish, object)}{new_line}')

# Speaks for it self:


print(f'{type_animal} {msg_subclass_of} {type_object}: {issubclass(type_mammal, type_object)}')
print(f'{type_mammal} {msg_subclass_of} {type_animal}: {issubclass(type_mammal, type_animal)}')
print(f'{type_fish} {msg_subclass_of} {type_animal}: {issubclass(type_fish, type_animal)}{new_line}')

# Inheritance is a good thing, but can lead to bad things checkout: MultiLevelInheritance.py
