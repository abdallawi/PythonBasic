
def first_method():
    print('invoked first_method')


first = first_method
print(first())

def second_method():
    return first


sec = second_method
# The function sec() return a reference to a function
print(sec())

print(first)
# The function will be invoked
print(sec()())