def total_sum(n, func):
    total = 0
    for num in range(1, n+1):
        total += func(num)
    else:
        return total

def square(x):
    return x*x

def cube(x):
    return x**3


number = 5
print(f'Result square: {total_sum(number, square)}')
print(f'Result cube: {total_sum(number, cube)}')


