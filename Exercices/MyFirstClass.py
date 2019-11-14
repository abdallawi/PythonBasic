class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def __str__(self):
        return f'{self.fname.title()} {self.lname.title()}, {self.age} jaar'

    # def get__fname(self):
    #     return self.__fname
    #
    # def set_fname(self, name):
    #     self.__fname = name

    def __add__(self, x):
        self.age += x

class Student(Person):

    def __init__(self, matricule, *kds):
        super(Student, self).__init__(*kds)
        self.matricule = matricule

    def __str__(self):
        return f'{self.fname.title()} {self.lname.title()}, {self.age} jaar, matricule {self.matricule}'


rania = Person('el abdellaoui', 'rania', 8)
fares = Student( 25166, 'el abdellaoui', 'Mohamed fares', 8)
noureyne = Student( 25167, 'el abdellaoui', 'noureyne', 2)
print(rania)
print(fares)
print(noureyne)
# fares + 2
# print(fares.get__fname())
# noureyne.set_fname('Nounayne')
# print(noureyne.get__fname())
print(fares.__class__)
print(rania.__class__)



