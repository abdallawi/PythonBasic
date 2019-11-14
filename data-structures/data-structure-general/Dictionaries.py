# In Python we have a very powerful data structure to hold key-value pairs: dictionaries.
# We can only use immutable objects as the key [so mostly string is used], the value can be whatever no limitations.

# Makes sense:

new_line = '\n'
key_x = 'x'
key_y = 'y'
key_z = 'z'
invalid_key = 'invalid key'
val_x_msg = 'The value of x is:'
mem_loc_msg = 'memory location:'

# Let's start by making one to play around with:

point = {key_x: 1, key_y: 2}  # We're using a string as a key and an integer as the value.


# Just as there are functions to create lists, tuples and sets there is a builtin function to make dictionaries:

sec_point = dict(x=1, y=2)  # keyword argument are a bit cleaner then the double/single quotes.


# We can print some information about these objects:

print(F"{point} {mem_loc_msg} {id(point)}")
print(F"{sec_point} {mem_loc_msg} {id(sec_point)}", new_line)


# we can search values according to keys stating them as index with the brackets notation:

print(F"{val_x_msg} {point['x']}")


# We can't use numeric indexes like we do with lists, so the following syntax will trow an exception:

# print(F"{'Value of first element:'} {points[0]}")  # uncomment to see the exception in action :)


# Of course we can change the value as follows:

point[key_x] = 5


# Lets see if we modified the value:

print(F"{val_x_msg} {point[key_x]}", new_line)


# We can add key-value pairs in the same way:

point[key_z] = 14


# Lets see if that worked:

print(F"{point} {mem_loc_msg} {id(point)}", new_line)


# If you would search for a value using an invalid key we get a KeyError, but good programmers check before:

if invalid_key in point:
    print('Never gonna get here, so no error for you! Good job', point[invalid_key])


# Better even would be to use the get() method, this will return None if the key is invalid [uncomment to see diff]:

print(F"{'Value returned when using a invalid key:'} {point.get(invalid_key)}", new_line)
# print(points.get(invalid_key, points[key_x]))  # We return a default value only if the key is not found.


# We can also use the del statement to take a key-value pair out of our dictionary:
del point[key_x]


# Lets take another look:

print(F"{point} {mem_loc_msg} {id(point)}", new_line)


# We can loop over our keys, and use the key to retrieve the corresponding value:

for key in point:
    print(F"{'Key:'} {key} {'Value:'} {point.get(key)}", new_line)


# We can also iterate over our dictionary returning a tuple holding the key and value:

for t in point.items():
    print(t)
else:
    print()

# We can of course unpack the tuple:

for key, value in point.items():
    print(F"{'The key:'} {key} {'holds the value:'} {value}")

