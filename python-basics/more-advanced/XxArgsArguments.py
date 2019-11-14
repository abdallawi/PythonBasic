# Lets simulate some db action with python 3.7 :D:

# We can write a function for that:

# Instead of giving it an arbitrary amount of arguments,
# we use an arbitrary amount of keyword arguments.

# let me google that for you: https://duckduckgo.com/?q=python+keyword+arguments&atb=v120-7&ia=web


def save_user(**user):
    print(user)


save_user(id=1, name='Admin')  # printout holds multiple key/value pairs


# The printout from above is actually a Python dictionary
# JS devs should recognize this format it looks like an object in JavaScript

# Okay lets wrap it up and finish our functions:

def save_user_show_id(**user):
    print(user['id'])


save_user_show_id(id=1, name='Admin')


def save_user_show_name(**user):
    print(user['name'])


save_user_show_name(id=1, name='Admin')
