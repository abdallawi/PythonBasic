path = '../txt-files/rand.txt'
sec_path = '../txt-files/second_file.txt'

try:
    with open(path) as file:
        print('File is opened.')
except OSError:
    print()


try:
    with open(path) as file, open(sec_path) as sec_file:
        print('File is opened.')
        # if an object has these 2 methods[L20/L21] it means that it can be used in the with statement.
        # These objects support contact management protocol, more about this in the class package.

        # file.__enter__()  # We call these kind of methods, magic methods.
        # file.__exit__()
except OSError:
    print('IO exception occurred, fix that shit bro!')