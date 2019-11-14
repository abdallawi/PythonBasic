from timeit import timeit
code1 = """
def calculate_x_factor(age):
    if age <= 0:
        raise ValueError('Age cannot be 0 or less.')
    return 42 / age


try:
    calculate_x_factor(-27)
except ValueError as ve:
    pass  # To speed up our code ;)

"""

code2 = """
def calculate_x_factor(age):
    if age <= 0:
        return None
    return 42 / age


x_factor = calculate_x_factor(-27)
if x_factor == None:
    pass
"""

msg = 'Excution time of our code: '

print(f'{msg} code 1 | ', {timeit(code1, number=10_000)})
print(f'{msg} code 2 | ', {timeit(code1, number=10_000)})