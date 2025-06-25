class Car:
    def __init__(self, model: str):
        self.model = model

    def start(self):
        print(f'{self.model} is starting!')


class Driver:
    def __init__(self, name):
        self.name = name

    def drive(self, car):
        car.start()


my_car = Car('Mercedes')
driver = Driver('Mario')

driver.drive(my_car)
