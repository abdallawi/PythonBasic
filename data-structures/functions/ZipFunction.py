# We will make 2 lists to play around with:

list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]

# If wanted to combine them in a single list holding Tuple values:
# [(1, 10), (2, 20), (3, 30)]  # taking the first element out of both list combine them in a Tuple, etc...:

# We can't use the map function or list comprehension because both of those work only on a single list!
# Luckily for us the built in function zip exists [Takes multiple iterable objects as argument/s].

# Good practice guys:

combined_message_2_lists = 'Combined list created out of objects from same index out of 2 different lists:'
combined_message_3_iterables = 'Combined list created out of objects from same index out of 3 different iterables:'
new_line = '\n'

# You guessed it, this function returns a zip object so we need to cast to list:

list_combined_out_other_lists = list(zip(list1, list2))
print(F'{combined_message_2_lists} {list_combined_out_other_lists}', new_line)

# We can do this with as many iterable objects as desired:

list_combined_out_iterables = list(zip(list1, list2, 'ALEX'))
print(F'{combined_message_3_iterables} {list_combined_out_iterables}', new_line)
