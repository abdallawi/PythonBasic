# Let us have a look at the unpacking operator:
numbs = [x for x in range(1, 11)]  # Making a list to play with, remember second argument range is exclusive

# Nothing new here, print the result:
print(numbs)

# But we see that we print a string representation of our list, so what if we want the individual numbers of our list:
print(*numbs)  # This is the same as the JS spread operator ...


mix_it_up = [*range(1, 28), *"Python Courses"]

# Now print the result:
print(*mix_it_up)

# We can easily use this operator to combine multiple lists:
first_one = [*range(6)]
second_one = [*range(4, 9)]
combined_one = [*first_one, *second_one]

# Print the result:
print(combined_one)

# We can also use this unpacking operator with Dictionaries lets make 2 to play around with:

first_dict = {'x': 1, 'y': 2}
second_dict = {'x': 42, 'y': 27, 'z': 18}

# The Python interpreter sees the double keys in our dictionaries and takes the last key value pair as the new entry.

combined_dict = {**first_dict, **second_dict}  # We could of course add even other values here.

# Lets see what we get:
print(combined_dict)


