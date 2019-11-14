# # Lets make a list to play with:
#
# names = ['Kenan', 'Bart', 'Patrick', 'Wouter', 'Olmo', 'Alex']
#
# # Lets use a for loop to check if we have a name that starts with A, in most languages we do:
#
# found = False
# for name in names:
#     if name.startswith('A'):
#         print(name)
#         found = True
#         break  # If we do we use break[only interested in first name we find, for loops are resource expensive]
#
# if not found:
#     print('No name found starting with A')  # Triggered if no break is given by the time for loop ends
#
# # Now lets see the Python way and see what it has in store for us:
#
# for name in names:
#     if name.startswith('X'):
#         print(name)
#         break
# else:  # Else statement gets triggered if the for loop is not broken with the break keyword
#     print('No name found starting with X')
digits = [0, 1, 5]

for i in digits:
    print(i)
    if i == 1:
        break
else:
    print("No items left.")