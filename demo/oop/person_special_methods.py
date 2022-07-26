class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __gt__(self, other):
        return self.age > other.age

    def __int__(self):
        return self.age


p1 = Person("Ellison", 50)
p2 = Person("Ellison", 40)
p3 = Person("Tom", 35)

print(int(p1) + int(p2))   #  p1.__int__()

print(p1, str(p1))  # p1.__str__()
print(p1 == p2)  # p1.__eq__(p2)
print(p1 > p3)  # p1.__gt__(p3)
print(p2 < p3)  # p1.__gt__(p3)

for p in sorted([p1, p2, p3]):
    print(p)
