# 5. Write a Python program which accepts the user's first and last name
# and print them in reverse order with a space between them.

firstName = input("Enter your first name\n")
lastName = input("Enter your last name\n")

print(f'Salut {lastName} {firstName}')

# Using lambda
full_name = lambda x, y: f'Full name: {y.title()} {x.title()}'

print(full_name(lastName, firstName))


