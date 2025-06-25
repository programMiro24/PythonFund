class Person:
    species = "Human"

    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("Peter", 25)
person2 = Person("John", 44)

print(person1.species)
print(person2.species)
