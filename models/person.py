class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def __del__(self):
        print("Destructor called for Person!")

person = Person("Zaib", "36")

print(person.get_name())