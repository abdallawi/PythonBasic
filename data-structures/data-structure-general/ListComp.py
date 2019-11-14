
my_list = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

for n in range(len(my_list)):
    print(my_list[n])

my_other_list = [x**2 for x in range(1,11)]

for n in range(len(my_other_list)):
    print(my_other_list[n])