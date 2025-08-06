money_for_search = float(input())
numbers_of_users = int(input())

total_money = 0

for number_of_user in range(1, numbers_of_users + 1):
    number_of_user_search = int(input())
    money_for_user = money_for_search
    if number_of_user_search == 1:
        continue
    if number_of_user % 3 == 0:
        money_for_user *= 3
        if number_of_user_search > 5:
             money_for_user *= 2
    elif number_of_user_search > 5:
        money_for_user *= 2
    money_for_user *= number_of_user_search
    total_money += money_for_user

print(f"Total money earned: {total_money:.2f}")
