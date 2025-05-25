total_price = 0
numbers_of_orders = int(input())
for order in range(numbers_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100.00:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_per_day > 2000 or capsules_per_day < 1:
        continue
    price = price_per_capsule * capsules_per_day * days
    print(f"The price for the coffee is: ${price:.2f}")
    total_price += price
print(f"Total: ${total_price:.2f}")
