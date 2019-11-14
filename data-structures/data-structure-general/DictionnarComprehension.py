random_chars = { x: chr(x*50) for x in range(11) }

print(random_chars)

for key, value in random_chars.items():
    print(f'key: {key} holds the value: {value}')

rand_tuples = ( x for x in range(11))
print(type(rand_tuples), rand_tuples)

