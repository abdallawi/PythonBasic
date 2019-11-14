from random import randint


def function_name(parameter_list):
    pass


def increment_pass(number, by):
    return number + by


def increment_by_one(number, by=1):
    return number + by


def pass_multiple_values():
    return randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)


print(pass_multiple_values())

first, second, *third = pass_multiple_values()

print(first)
print(second)
print(third)


def sum_arg(*numbers):
    """Demonstarte docstrings and does nothing really."""

    return sum(numbers)


print(sum_arg(10, 2, 3))

print(sum_arg())
print(sum_arg(10))
print(sum_arg(10, 2, 3))

tup = ('pyton',)*3
print(tup)
