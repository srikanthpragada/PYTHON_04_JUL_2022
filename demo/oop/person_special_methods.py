class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


p1 = Person("Ellison", 50)
p2 = Person("Ellison", 50)

print(p1, str(p1))  # p1.__str__()
print(p1 == p2)     # p1.__eq__(p2)
# print(p1 > p2)

