n = int(input())
cars = {}
for car_number in range(n):
    car, mileage, fuel = input().split('|')
    cars[car] = {'mileage': int(mileage), 'fuel': int(fuel)}

while (command := input()) != 'Stop':
    parts = command.split(' : ')
    action, car = parts[0], parts[1]
    if action == 'Drive':
        distance, fuel_needed = map(int, parts[2:])
        if cars[car]['fuel'] < fuel_needed:
            print("Not enough fuel to make that ride")
        else:
            cars[car]['mileage'] += distance
            cars[car]['fuel'] -= fuel_needed
            print(f"{car} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")
        if cars[car]['mileage'] >= 100_000:
            print(f'Time to sell the {car}!')
            cars.pop(car)

    elif action == 'Refuel':
        fuel_amount = int(parts[2])
        current_fuel = cars[car]['fuel']
        added_fuel = min(75 - current_fuel, fuel_amount)
        cars[car]['fuel'] += added_fuel
        print(f"{car} refueled with {added_fuel} liters")

    elif action == 'Revert':
        kilometers = int(parts[2])
        if cars[car]['mileage'] - kilometers < 10_000:
            cars[car]['mileage'] = 10_000
        else:
            cars[car]['mileage'] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")

for car, data in cars.items():
    print(f"{car} -> Mileage: {data['mileage']} kms, Fuel in the tank: {data['fuel']} lt.")
