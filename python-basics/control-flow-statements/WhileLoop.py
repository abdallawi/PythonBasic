# from random import randint
# # Variables oh how I love to play with them:
#
# guess = 0
# answer = randint(0,100)
#
# # Mini game that uses user input to check vs a hardcoded answer, when guessed correctly game is ended:
#
# while answer != guess:
#     guess = int(input('Make a guess[0,100]: '))  # We know will get a string back so we cast it to integer
#     if answer < guess:
#         print('lower')
#     else:
#         print("Higher")
#
# else:  # Only triggered if the while loop is ended without a break statement
#     print('You guessed right!')

counter = 0
while counter < 5:
    print("Inside the loop")
    counter += 1
    if counter == 3:
        break
else:
    print("Inside else: Only triggered if the while loop is ended without a break statement")