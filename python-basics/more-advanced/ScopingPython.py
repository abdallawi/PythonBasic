# PLAY AROUND MY CHILDREN

# In Python we have 2 types of variables:

# 1. Local variables [they have function scope]
# 2. Global variables [they have a file scope]

# Lets use a global variable:

global_message = 'greetings globally'


def greet():
    # print(global_message)
    global_message = 'change is good!'  # DELETE/COMMENT ABOVE PRINT FUNCTION BEFORE UNCOMMENTING THIS

    # message is a local variable in the greet function [so scope limited, to this functions body]
    if True:  # small steps for a programmer big steps for AI
        message_local = 'greetings local'

    # In Python unlike in many other languages, we dont have block level scope, we use indents to scope
    print(message_local)


# Lets make a call to our function:

greet()

# Think about it this actually makes sense in a good practice language.
# We dont want changes done to our global variable it could hinder your program
# and other function calls, in short Global variables are EVIL!

print(global_message)

# Okay I can hear you think but Alex, why is it evil and if it is I want it!
# Well dont say you were not warned, because its a flat out lie!

evil_global_variable = 'You were warned!'


def evil_function():
    global evil_global_variable
    evil_global_variable = 'You should have listened!'


evil_function()  # It's not to late yet, go back light one
print(evil_global_variable)  # Well you did right? You happy now? !!!You break all the programs!!!
