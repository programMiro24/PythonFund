divisor = int(input())
boundary = int(input())
maximum = ""
for current_number in range(boundary, divisor-1, -1):
    if current_number % divisor == 0:
        maximum = current_number
        break
print(maximum)
