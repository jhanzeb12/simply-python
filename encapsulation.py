class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        if value is None:
            return Exception("Name cannot be null")
        self.__name = value

    @staticmethod
    def print_attribs():
        print(f"These are values")

p1 = Person('Jahanzeb', 30)

print(Person.print_attribs())
p1.Name = None
print(p1.Name)