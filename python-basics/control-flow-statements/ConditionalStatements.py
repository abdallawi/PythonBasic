# Variable to play with
age = int(input('Give your age:\n'))

# IMPORTANT:
# TABS AND SPACES DONT MIX IN PYTHON

# Let's take a look at a conditional statement:

if age >= 18:  # Because we don't have {} in Python we dont need to argue where to put them for 2 decades.
    print("You're an:")
    print('Adult')  # indented code belongs to if statement

elif age >= 13:  # To start a elsif it needs to be indented the same as the if statement
    print("You're a teenager")

else:  # And of course we can use the else statement.
    print('Child')

# This part is after our conditional statements...
print("The if/elif/else all done!")

# Ternary operator
message = 'Eligible' if age >=18 else 'Not elegible'
print(message)


# If you want to use empty conditional statements[as a placeholder till implementation] you can use the pass keyword:

if age > 101:
    pass  # Won't compile otherwise
else:
    pass
