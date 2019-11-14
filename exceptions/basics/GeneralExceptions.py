# When we awesome programmers write our code many things could go wrong,
# our programs can encounter allot of different exceptions. It is our duty to handle this of course.

# Lets create an example that crashes our application:

numbers = [1, 2]

# BAD PROGRAMMING:

# print(numbers[3])  # Uncomment to see the world burn :D

# Okay the above code should not slip in to production code, because it would be bad code!
# But what to do with the unexpected like user input for example?

# Hopefully our user knows what to do; and which data we need said no one ever:

age = int(input('Please fill in your age: '))  # First time asked the age in console give int to get passed this!

# For these kind of situations we have the try-except block:

try:
    age = int(input('Please fill in your age: '))  # Remember the input function always returns a string!
except ValueError:
    print('You did not enter a valid age!')
else:
    print('Executed if and only if there was no exception thrown')  # Test it when in doubt :D

print('Executions continues')  # Because we took care of a possible exception we're sure to arrive here whatever happens

# Lets do this all over again but do something more meaningful then a printout

try:
    age = int(input('Please fill in your age: '))
except ValueError as ve:
    print(type(ve))  # Instead of printing this to the console most of the time
else:
    print('Executed if and only if there was no exception thrown')

# Here is an overview of the Python exception hierarchy:
# More info can be found here: https://docs.python.org/3/library/exceptions.html

# TL;DR
"""
BaseException0.
 +-- SystemExit
 
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
"""
