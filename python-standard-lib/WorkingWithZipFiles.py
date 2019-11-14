from pathlib import Path
from zipfile import ZipFile

# Makes sense:

zip_f_name = 'standard_lib_python.zip'
write = 'w'
new_line = '\n'
zipped_resources = Path('./zipped-jpg/test_pictures.zip')

# We create a Path instance so that we can later zip our project into a zipfile:

project_path = Path('/home/eliot/PycharmProjects/python_basics/python-standard-lib/jpg')

# Will create an empty zipfile in the current folder, if one exist it will be overwritten:

zip_f = ZipFile(zip_f_name, write)

# And now this is how we can store our content in that zip file:

for path in project_path.rglob('*.*'):
    zip_f.write(path)

# We are good programmers and that's why we close our resources when we're done handling them:

zip_f.close()  # As long as this is not closed you can't read from this zipfile, it will throw not a zipfile exception!

# We can also read from our zipfile:

with ZipFile(zip_f_name) as zipped_folder:
    print(zipped_folder.namelist(), new_line)  # Take a look at all files in the zip folder.

    # We can collect all the names into a list
    name_files = [name for name in zipped_folder.namelist()]

    for name in name_files:
        info = zipped_folder.getinfo(name)  # Here we get an object back holding info about our zipped file
        print(name)

        # And we can use that info object to show us the original and the compressed size:

        print(f"Original size: {info.file_size}")
        print(f"Compressed size: {info.compress_size}{new_line}")
        # If you want to see a diff result simply change the variable zip_f_name in zipped_resources on line 30.
