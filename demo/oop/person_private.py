class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age


p1 = Person("Ellison", 50)
p1.set_age(40)
print(p1._Person__age)
print(p1.get_age())
print(p1.__dict__)
