# Lets define a function:


def multiply(a, b):
    return a * b


# So far so good, lets call it:

multiply(2, 5)


# But what if we want to give a variable amount of arguments
# So lets define a new function, we use an astrix as a way of saying
# multiple arguments are allowed:


def multiply_list_1(*list_values):
    print(list_values)  # Prints out a Tuple because the astrix converts params to Tuple


multiply_list_1(2, 4, 5, 9)
multiply_list_1(1)
multiply_list_1(1, 8, 5, 4)


# Lets change our function so that it actually multiplies the given arguments:
def multiply_list_2(*list_values):
    total = 1
    for number in list_values:
        total *= number  # We cant edit a Tuple but we can use its value
    return total


print(F'{"The sum is: "}{multiply_list_2(2, 4, 5, 9)}')
print(F'{"The sum is: "}{multiply_list_2(1)}')
print(F'{"The sum is: "}{multiply_list_2(1, 8, 5, 4)}')
