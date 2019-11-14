def cubes_sum(num):
    total = 0
    for i in range(1, num):
        total += i**3
    return total


num = int(input('give a number\n'))
print("Sum of cubes: ", cubes_sum(num))

