# We use the square bracket notation to make a list[or a sequence of objects]:

empty_list = []
print(empty_list)

# Inside our list we can have a sequence of any type of objects:
list_of_strings = list()
list_of_strings = ['Fares', 'is', "my", 'beloved', 'son', 'life']
list_strings = ['Alex', 'working', 'too', 'hard', ',', 'but', 'can\'t', 'help', 'it']
list_numbers = [42, 420]
list_booleans = [True, False, False, True]

# Printout time:

print(list_of_strings)
print(list_strings)
print(list_numbers)
print(list_booleans)

# Of course we can also have a list of lists:

list_of_lists = [list_strings, list_numbers, list_booleans]
print(list_of_lists)

# Or we can get the same result as follows, it is called a matrix btw:

list_matrix = [[1, 2], [85, 97]]
print(list_matrix)

# What if you wanted a list with a hundred times the value 0:

list_zero = ['*' for n in range(100)]
print(list_zero)

# Want it event shorter and sweeter:

zeroes = [0] * 100
print(zeroes)

# We can also concatenate different list together as follows:

list_combined = list_numbers + list_strings + list_matrix  # Different data types can be combined
print(list_combined)

# You can also make list like so:

list_exclusive_20 = list(range(20))
list_chars = list('Alexander')

# See what we get:
print(list_exclusive_20)
print(list_chars)

# How big is our list, well lets print it out using the len() function:
print(F'{"The list of chars contains:"} {len(list_chars)} {"values."}')
