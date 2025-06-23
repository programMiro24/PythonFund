MAX_HEALTH = 100

health = MAX_HEALTH
bitcoins = 0

rooms = input().split('|')  # rat 10|bear 20... -> ["rat 10", "bear 20"]

for i in range(len(rooms)):
    command, value = rooms[i].split()  # "rat 10" -> ["rat", "10"]
    value = int(value)

    if command == "potion":
        healed = min(value, MAX_HEALTH - health)  # current_health = 75,value = 50->min(50, 100 - 75) = min(50, 25) = 25
        health += healed
        print(f"You healed for {healed} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += value
        print(f"You found {value} bitcoins.")
    else:
        health -= value
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {i + 1}")
            break

else:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
