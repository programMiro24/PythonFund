class Person:
    def __init__(self, first_name, last_name, age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def person_info(self):
        return f'{self.first_name} {self.last_name}, age: {self.age}'


ivan = Person('Ivan', 'Ivanov', 35)
gosho = Person('Gosho', 'Georgiev', 22)

ivan.age += 10
print(ivan.age)
