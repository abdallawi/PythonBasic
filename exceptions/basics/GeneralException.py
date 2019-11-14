numbers = [1, 2]
# print(numbers[3])

try:
    age = int(input('Please fill in your age:\n'))
except ValueError:
    print("You did not enter a valid age")
else:
    print('excuted if and only if no error is thrown.')

print('Execution continues?')