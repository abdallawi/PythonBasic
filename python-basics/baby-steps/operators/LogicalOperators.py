# Lets make a variable to play with:

name = 'Alex'
empty_name = ''
not_an_empty_name = ' '

# In Python we have 3 logical operators:

# and
# or
# not

# Lets take a look at some examples with not operator:

if not name:  # We are using the fact that an empty string is Falsy
    print("name is empty")

if not empty_name:
    print("empty_name is empty")

if not not_an_empty_name:
    print("not_an_empty_name is empty")

# To check if the value of our variable is not simply whitespaces:

if not not_an_empty_name.strip():  # Variable name is a mind fuck!!
    print("not_an_empty_name is empty")

# Create a new variable to play with:

age = 12

# Now lets use the and operator:

if age >= 18 and age < 65:  # 18 <= age < 65 This is called chaining comparision operators
    print("Eligible")
