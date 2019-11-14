from pathlib import Path

# Makes sense:

new_line = '\n'

# In this class we will be working with directories hence the name of the class.
# I will be going over the most used methods, so lets dive in to the code:

# First we will need a Path object that represents a directory:

path_root = Path(r'C:\Users\abdelmounaim\Documents\MyDesktop\python file\python_basics')
path_new_dir = path_root / 'resources'

# If you want to see if a certain directory exist you can do it like this:

print(f"{new_line}The path {path_root} is a directory that exists: {path_root.exists()}{new_line}")
print(f"{new_line}The path {path_new_dir} is a directory that exists: {path_new_dir.exists()}{new_line}")

# Lets create a new directory:

path_new_dir.mkdir()

# Lets delete it right away like this:

path_new_dir.rmdir()

# If you want to rename it you can do like so:

path_new_dir.mkdir()  # Create a directory to rename
path_new_dir.rename('test_renaming')  # Rename the directory
path_new_dir = Path('./test_renaming')  # Store the new path
path_new_dir.rmdir()  # delete the directory to keep it clean

# One of the more useful and interesting methods is the iterdir method that returns a generator object containing
# all files and subdirectories of our directory represented by the path object.

iter_dir = path_root.iterdir()

# So now we can iterate over it:

for i in iter_dir:
    print(i)

# Now if your directory is not to big you could put it in a list,
# this can be handy if you wanna work with it in the future:

list_dir_cont = [p for p in path_root.iterdir()]

# We actually have 2 kind of paths: PosixPath and WindowsPath [i'm working on linux, so I get a PosixPath]
# print()
# print(list_dir_cont)

# We can even do filtering on this list comprehension:

files_in_dir = [p for p in path_root.iterdir() if p.is_file()]
sub_dirs_in_dir = [p for p in path_root.iterdir() if p.is_dir()]  # add directory in path, then uncomment :D
print(files_in_dir)
print(sub_dirs_in_dir)
path_home = Path.home()

# py_files = [p for p in path_home.rglob('*.py')]

# print(py_files)
