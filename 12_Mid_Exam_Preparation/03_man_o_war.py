def is_valid_index(index: int, _list: list[int]) -> bool:
    return 0 <= index < len(_list)


def get_data(_list) -> list[int]:
    return [int(el) for el in _list.split()[1:]]


def input_ships():
    return [int(el) for el in input().split(">")]


pirate_ship = input_ships()
war_ship = input_ships()
max_health = int(input())  # 100
repair_health_threshold = max_health * 0.20  # 100 * 0.2 = 20
while True:
    # Repair 10 20 30
    command = input()
    if command == "Retire":
        pirate_ship_sum = sum(pirate_ship)
        war_ship_sum = sum(war_ship)
        print(f"Pirate ship status: {pirate_ship_sum}")
        print(f"Warship status: {war_ship_sum}")
        break
    if command.startswith("Fire"):
        # Fire 10 20 -> ['Fire', '10', '20'][1:] -> ['10', '20'] -> [10, 20]
        idx, damage = get_data(command)
        if not is_valid_index(idx, war_ship):
            continue
        war_ship[idx] -= damage
        if war_ship[idx] <= 0:
            print("You won! The enemy ship has sunken.")
            break
    elif command.startswith("Defend"):
        start_idx, end_idx, damage = get_data(command)
        if not (is_valid_index(start_idx, pirate_ship) and is_valid_index(end_idx, pirate_ship)):
            continue
        for i in range(start_idx, end_idx + 1):
            pirate_ship[i] -= damage
            if pirate_ship[i] <= 0:
                print("You lost! The pirate ship has sunken.")
                exit()
    elif command.startswith("Repair"):
        idx, health = get_data(command)
        if not is_valid_index(idx, pirate_ship):
            continue
        pirate_ship[idx] += min(health, max_health - pirate_ship[idx])
    elif command.startswith("Status"):
        for_repair = sum(1 for sec in pirate_ship if sec < repair_health_threshold)  # sum([1, 2, 3]) -> 6
        print(f"{for_repair} sections need repair.")
