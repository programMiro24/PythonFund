number = int(input())
number_to_string = str(number)
digits = []
for digit in number_to_string:
    digits.append(digit)
digits.sort(reverse=True)
for digit in digits:
    print(digit, end="")