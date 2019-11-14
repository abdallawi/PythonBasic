# You remember the sort function where we pass our function:

# Quick reminder:

# A way of helping Python is giving it a value that is sortable,
# We can make a function to do that:

# def sort_item(item):
#     return item[1]  # Location of the price in our tuple, Python knows how to sort numbers


# Now we can use the sort method again:

# items.sort(key=sort_item)  # Our function is passed to the keyword argument key

# Lets see if our friend Python could with a little help:

# print(items)


# Now we can also do this with a lambda expression,
# Lets make a list of items:

items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 18),
    ('Product4', 42),
    ('Product5', 27),
    ('Product6', 29),
    ('Product7', 4)
]

# And now we want to sort them using our lambda expression:

# items.sort(key=lambda parameters:expression)  # Base syntax
items.sort(key=lambda item: item[1])
