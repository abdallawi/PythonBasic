from abc import ABC, abstractmethod

# We will continue with the example from the ExampleGoodInheritance.py class.
# This still has some issues!

# FIRST PROBLEM

# It is possible to create an instance of the Stream class, this would allow us to open and close a Stream.
# This is dangerous because we don't even know which stream we are dealing with!

# SECOND PROBLEM

# We have the same method read in all classes added[FileStream, NetworkStream, MemoryStream].
# It would be simpler to include this all ready in our Base Class.

# The class actually represents an abstract idea, and that would be more suited for an Abstract Base Class.

# You can see an abstract base class as a contract with all classes,
# this way we can make sure all sub classes have some behaviour and attributes in common and can add stuff if needed.


class InvalidOperationError(Exception):

    pass


class Stream(ABC):  # AbstractBaseClass ;)

    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError('Stream is already open!')
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError('Stream is already closed!')
        self.opened = False

    @abstractmethod  # All sub classes should give an implementation to this method!
    def read(self):
        pass


class FileStream(Stream):

    def read(self):
        print('Reading data from a file...')


class NetworkStream(Stream):

    def read(self):
        print('Reading data from a network...')


class MemoryStream(Stream):

    def read(self):
        print('Reading data from memory...')


# We can improve the manager said, I'll give anyone a bonus who can make this happen he said.
# Of course said the monkey, and wrote following class in a hurry:

class MakeBonus(Stream):

    def read(self):
        print('Reading data from bonus...')


# Lets see if our problem is fixed now:

# stream = FileStream()
#
# stream.open()
# stream.close()

# Shows demo to boss:                                    Comment line 74-77 to run the code beneath

bonus = MakeBonus()

bonus.open()
bonus.close()
