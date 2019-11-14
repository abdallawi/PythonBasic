from sys import getsizeof

# In Python we can use generator objects if we are working with big data sets or perhaps an infinite input of data.
# We actually don't want to store al this data in memory, lets take a look at an example:

values = [x * 2 for x in range(1_000_000)]

# Lets take a look at the byte size of this list using the sys module:
print('List size in bytes: ', getsizeof(values))

# Below we can see the syntax for creating a generator object:

values = (x * 2 for x in range(1_000_000))  # Just like lists, generator objects are iterable

# Lets take a look at the size of our generator obj:
print('Generator object size: ', getsizeof(values))
# INFO: Instead of storing all our values in memory, the value gets changed every iteration.

# What happens if we enlarge our generator object:

values = (x * 2 for x in range(1_000_000_000))  # FUN FACT: A list this large would not work [out of memory]

# We again print our size expressed in bytes, can you guess what happens:
print('Bigger generator object size: ', getsizeof(values))  # What a shock! Not really of course :)

# This has some downsides as well, when we use a generator object we can't see how many object we will be working with:

try:
    print(len(values))

except TypeError as te:  # We declare te so that we can do something like print the exception in code below
    print(te)
