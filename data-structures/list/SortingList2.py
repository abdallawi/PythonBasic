from random import  randint

def print_list(*args):
    if args:
            for single_list in args:
                print(f'id {id(single_list)}: {single_list}')


new_line = '\n'

numbers = [randint(0,100) for number in range(10)]

# print_list(numbers)

# numbers.sort()
# print_list(numbers)
#
# numbers.sort(reverse=True)

print_list(numbers)

returned_new_list = sorted(numbers)
print_list(returned_new_list)

returned_new_list = sorted(numbers, reverse=True)
print_list(returned_new_list)