number = float(input())
type_number = ""
second_type_number = ""

if number == 0:
    type_number = "zero"
elif number < 0:
    type_number = "negative"
else:
    type_number = "positive"

if abs(number) > 1_000_000:
    second_type_number = "large"
elif abs(number) < 1 and abs(number) != 0:
    second_type_number = "small"
print(f"{second_type_number} {type_number}")
