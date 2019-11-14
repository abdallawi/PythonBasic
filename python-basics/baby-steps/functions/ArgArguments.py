def multiply(a, b):
    return a*b


print(multiply(2, 5))

def multiply_list_1(*list_values):
    print(type(list_values), list_values)


multiply_list_1()
multiply_list_1(3)
multiply_list_1(1, 2, 5, 4)

def multiply_list_2(*list_values):
    total = 1
    for num in list_values:
        total *= num
    return total


msg_sum = "The sum is"

print(f'{msg_sum} {multiply_list_2(2, 4, 5, 9)}')
print(f'{msg_sum} {multiply_list_2(2, 4)}')
print(f'{msg_sum} {multiply_list_2(2,)}')


