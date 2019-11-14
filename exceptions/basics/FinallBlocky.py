path = '../txt-files/rand.txt'

try:
    file = open(path, 'w')
    file.write("Would be easy right")
except OSError as oe:
    print('Something went wrong with IO-operation')
finally:
    file.close()
