
class Person:
    age = 0
    name = "Jon"
    dob = "00/00/0000"
    def __init__(self, name):
        self.name = name
    def ageUp(self):
        self.age += 1

print("hey!")
p1 = Person("James") # constructor
p2 = Person("Jasmine")
p2.ageUp()
p2.ageUp()
print(p2.age)
print(p1.age)
