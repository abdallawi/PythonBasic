from sys import getsizeof

values = [x*2 for x in range(1_000_000)]

print('List size in bytes: ', getsizeof(values))

values = [x*2 for x in range(1_000_000_000)]
print('Generator obj in bytes: ', getsizeof(values))