import re

information = input()
pattern = r'(?i)([#|])([a-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'
matches = re.findall(pattern, information)
total_calories = sum([int(calories[3]) for calories in matches])
days = total_calories // 2_000
print(f"You have food to last you for: {days} days")

for item in matches:
    item_name = item[1]
    expiration_date = item[2]
    calories = item[3]
    print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")
