from abc import ABC, abstractmethod

# Polymorphism is based on the greek words Poly (many) and morphism (forms).
# We will create a structure that can take or use many forms of objects.


class UIControl(ABC):

    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):

    def draw(self):
        print('TextBox')


class DropDownList(UIControl):

    def draw(self):
        print('DropDownList')


# We will write a function draw that takes an instance and uses its draw method:

def draw_single(control):
    control.draw()  # Python only knows at runtime which kind of object it's getting.


# Does the same as function above but takes a list

def draw_multi(controls):
    for control in controls:
        control.draw()


# Lets make some instances:

tb = TextBox()
ddl = DropDownList()

list_ui = [tb, ddl]

# Lets test polymorphism out:

draw_single(tb)
draw_single(ddl)

print()

draw_multi(list_ui)
