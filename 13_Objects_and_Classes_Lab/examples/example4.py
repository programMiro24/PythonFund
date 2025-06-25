class Car:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f'The {self.make} {self.model} engine is starting.')

    def stop_engine(self):
        print(f'The {self.make} {self.model} engine is stopping.')


car1 = Car('Mercedes', 'S500', 2023)
car2 = Car('BMW', '750', 2021)
car3 = Car('Toyota', 'Rav4', 2020)

car1.start_engine()
