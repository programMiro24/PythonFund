class Car:
    def __init__(self, color: str, brand: str):
        self.color = color
        self.brand = brand

    def drive(self):
        print(f'The {self.color} {self.brand} is driving.')

    def refuel(self):
        print(f'The {self.color} {self.brand} is refueling with petrol.')


class ElectricCar(Car):
    def __init__(self, color: str, brand: str, battery_range: int):
        super().__init__(color, brand)
        self.battery_range = battery_range

    def refuel(self):
        print(f'The {self.color} {self.brand} is charging. Range{self.battery_range}')


petrol_car = Car('Red', 'Opel')

petrol_car.drive()
petrol_car.refuel()

electric_car = ElectricCar('Blue', 'Tesla', 500)
electric_car.drive()
electric_car.refuel()
