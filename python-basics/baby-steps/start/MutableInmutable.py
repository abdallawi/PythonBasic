# Reserving memory space:

x = 420

# Lets lookup the memory location:

print(id(x))

# String, boolean and Integers are immutable so the python interpreter
# will allocate a new memory location if we alter the value of a variable:

x = 42
print(id(x))

# Lists however are mutable objects:

list_numbers = [1, 2, 3]
print(id(list_numbers))

# Lets see what our memory address is after some changes:

list_numbers.append(4)
print(id(list_numbers))
