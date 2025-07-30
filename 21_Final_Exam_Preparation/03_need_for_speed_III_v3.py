# Function type of code?????
cars = {}

def drive_func(car, distance, fuel_needed):
    if cars[car]['fuel'] < fuel_needed:
        print("Not enough fuel to make that ride")
    else:
        cars[car]['mileage'] += distance
        cars[car]['fuel'] -= fuel_needed
        print(f"{car} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")
    if cars[car]['mileage'] >= 100_000:
        print(f'Time to sell the {car}!')
        cars.pop(car)

def refuel_func(car, fuel_amount):
    current_fuel = cars[car]['fuel']
    added_fuel = min(75 - current_fuel, fuel_amount)
    cars[car]['fuel'] += added_fuel
    print(f"{car} refueled with {added_fuel} liters")

def revert_func(car, kilometers):
    if cars[car]['mileage'] - kilometers < 10_000:
        cars[car]['mileage'] = 10_000
    else:
        cars[car]['mileage'] -= kilometers
        print(f"{car} mileage decreased by {kilometers} kilometers")

def cars_record(number_of_cars):
    for car_number in range(number_of_cars):
        car, mileage, fuel = input().split('|')
        cars[car] = {'mileage': int(mileage), 'fuel': int(fuel)}

def main_func(number_of_cars):
    cars_record(number_of_cars)
    while (command := input()) != 'Stop':
        parts = command.split(' : ')
        action, car = parts[0], parts[1]
        if action == 'Drive':
            distance, fuel_needed = map(int, parts[2:])
            drive_func(car, distance, fuel_needed)

        elif action == 'Refuel':
            fuel_amount = int(parts[2])
            refuel_func(car, fuel_amount)

        elif action == 'Revert':
            kilometers = int(parts[2])
            revert_func(car, kilometers)

    for car, data in cars.items():
        print(f"{car} -> Mileage: {data['mileage']} kms, Fuel in the tank: {data['fuel']} lt.")

n = int(input())
main_func(n)
