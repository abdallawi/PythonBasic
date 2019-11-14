# You know the drill, we need variables to play with:

numbers = list(range(1, 101))

# We can use a for loop:

for numb in numbers:
    print(numb)

# If we use the enumerate function we get a Tuple returned holding the index en value:

for numb in enumerate(numbers):
    print(F'{"index:"} {numb} {":value"}', '\n')  # Formatting used to improve readability

# Lets clean up the out print using the unpacking technique:

for index, numb in enumerate(numbers):  # Tuples can also be unpacked
    print(F'{"index:"} {index} {"|"} {"value:"} {numb}')
