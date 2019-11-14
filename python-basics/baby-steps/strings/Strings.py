
sentence = 'This is a litaral string'
sentence = "This is another one"

sentence = 'I\'m a Python fanatic'
sentence = "I'm a Python fanatic"

sentence = 'A not very long string \
that spans 2 physical lines '
#print(sentence)

# Let's make a variable to work with:

course_name = 'Python course'

# if we want to know how many chars a String contains:

print(len(course_name))

# if we want a certain char in a String we can do:

print(course_name[0])

# In python we can also use a negative index:

print(course_name[-1])

# We can also slice a String:

print(course_name[0:6])  # Second arg is exclusive

# this notation does the same
print(course_name[:6])

# And of course this is also possible
print(course_name[7:])

# The python interpreter will always reserve a new memory location for the char/s taken:

print(id(course_name))
print(id(course_name[:]))  # Why is this the same address ;) [mutable]
print(id(course_name[5:]))  # "New Value" so it needs his own memory address
