class Human:

    def __init__(self, surname, name, intelligence):
        self.suname = surname
        self.name = name
        self.intelligence = intelligence

    def __str__(self):
        return f'{self.name} {self.surname}'

    def __eq__(self, other):
        return self.name == other.name and self.surname==other.surname

    def __gt__(self, other):
        return self.intelligence > other.intelligence

    def __add__(self, other):
        if isinstance(other, Human):
            return self.intelligence + other.intelligence


first_human = Human('El Abadellaoui', 'Fares', 50000)
wise_old_man = Human('Smith', "Elliot", 420)

print(f'Human 1 and Human 2 have the same value: {first_human == wise_old_man}')
print(f'Human 1 is more advanced than the Human 2: {wise_old_man > first_human }')

print(f'Human 1 object id: {id(first_human)}')
print(f'Human 2 object id: {id(wise_old_man)}')

first_human.intelligence = 6800

print(f'Human 1 and Human 2 have the same value: {first_human == wise_old_man}')
print(f'Human 1 is more advanced than the Human 2: {first_human > wise_old_man }')

print(first_human+1)
print(first_human+wise_old_man)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}  y : {self.y}'

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


first_point = Point(14, 45)
sec_point = Point(84, 3)
combined_point = first_point + sec_point

print(combined_point)
