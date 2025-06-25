class Car:
    def set_model(self, model):
        self.model = model

    def set_color(self, color):
        self.color = color

    def display_info(self):
        return f'Model: {self.model}, Color: {self.color}'


car = Car()
car.set_model('Mercedes')
car.set_color('Black')
print(car.display_info())
