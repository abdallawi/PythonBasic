import sqlite3
import json
from pathlib import Path

# Makes sense:

json_file = Path('/home/eliot/PycharmProjects/python_basics/python-standard-lib/json-files/movies.json')
mov_db = '/home/eliot/PycharmProjects/python_basics/python-standard-lib/sqlite-db/mov_db.sqlite3'
data = json_file.read_text()
movies = json.loads(data)  # If this makes no sense go back to WorkingWithJSON.py

# We will learn how to work with SQLite in Python in this class.

# SQLite is a very lightweight database that we will use for storing data of an application,
# Often the technology of choice for smaller applications like the apps you use on your phone or tablet.

# So it allows us to store our data easily in an structured format like a table of rows and columns

# We will start by writing to our SQLite db, we will use a json file for storing:

with sqlite3.connect(mov_db) as conn:  # We need a connection object
    command = 'INSERT INTO Movies values(?, ?, ?)'  # This is SQL syntax but is out of scope :)
    for movie in movies:
        conn.execute(command, tuple(movie.values()))  # We need to convert our movie dictionary values to a tuple
    conn.commit()  # And commit when done iterating to write our changes to our database.

# The first time you run this code this will throw the sqlite3.OperationalError: no such table: Movies
# Don't panic this is normal you will need to install the sqlite3 db first:

# Link to download page: https://sqlitebrowser.org/dl/

# When done installing open up DB Browser for SQLIte

# Click Open Database

# Select the mov_db.sqlite3 file then click Open in the bottom right corner

# Click Create Table in the top left corner

# Call it Movies

# Click on the Add field button, and create the following fields:

# Name          Type        Not  PK  Al  U  Default         Check

# Id            INTEGER          x
# Title         TEXT        x
# Year          INTEGER     x

# Click Ok

# Click the Write Changes button

# Rerun your code :D, when you get no error everything went well.

# Select the Movies Table, and change the tab from Database Structure to Browse Data.
# Now you should see your movie data in the sqlite db, whoop whoop!

# We will now take a look at reading from an SQLite db, first comment the code on line 21-25:

with sqlite3.connect(mov_db) as conn:
    command = 'SELECT * FROM Movies'
    # More info about cursor objects can be found here: https://docs.python.org/3.7/library/sqlite3.html#sqlite3.Cursor
    cursor = conn.execute(command)
    for row in cursor:
        print(row)

# Want to find out more about SQLite db and how to interact with them : https://docs.python.org/3.7/library/sqlite3.html
