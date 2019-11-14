# 7. Write a Python program to accept a filename from the user and print the extension of that
def get_extension(fname):
    if '.' not in fname:
        ext = 'No extension'
    else:
        dot_pos = fname.find('.')
        if dot_pos == len(fname)-1:
            ext = 'No extension'
        else:
            ext = fname[dot_pos + 1:]
    return ext


filename = input('Enter a file name: \n')
extension = get_extension(filename)
print(extension)

