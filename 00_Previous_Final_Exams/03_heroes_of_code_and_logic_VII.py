MAX_AMOUNT = 200
MAX_AMOUNT_HP = 100
numbers_of_heroes = int(input())
heroes = {}
for number_of_hero in range(numbers_of_heroes):
    hero_data = input().split(" ")
    hero_name = hero_data[0]
    hit_points, mana_points = map(int, hero_data[1:])
    heroes[hero_name] = {"hit_points": hit_points,
                         "mana_points": mana_points}

while (command := input()) != "End":
    command = command.split(' - ')
    action = command[0]
    hero_name = command[1]
    if action == "CastSpell":
        mana_points_needed = int(command[2])
        spell_name = command[3]
        if heroes[hero_name]['mana_points'] >= mana_points_needed:
            heroes[hero_name]['mana_points'] -= mana_points_needed
            mana_points_left = heroes[hero_name]['mana_points']
            print(f'{hero_name} has successfully cast {spell_name} and now has {mana_points_left} MP!')
        else:
            print(f'{hero_name} does not have enough MP to cast {spell_name}!')
    elif action == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]
        heroes[hero_name]['hit_points'] -= damage
        current_hp = heroes[hero_name]['hit_points']
        if heroes[hero_name]['hit_points'] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
        else:
            heroes.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")
    elif action == "Recharge":
        amount = int(command[2])
        current_mp = heroes[hero_name]['mana_points']
        recharge = min(MAX_AMOUNT - current_mp, amount)
        heroes[hero_name]['mana_points'] += recharge
        print(f"{hero_name} recharged for {recharge} MP!")
    elif action == "Heal":
        amount = int(command[2])
        current_hp = heroes[hero_name]['hit_points']
        heal = min(MAX_AMOUNT_HP - current_hp, amount)
        heroes[hero_name]['hit_points'] += heal
        print(f"{hero_name} healed for {heal} HP!")

for hero_name, hero_data in heroes.items():
    current_hp, current_mp = int(hero_data['hit_points']),\
                              int(hero_data['mana_points'])
    print(f"{hero_name}\n  HP: {current_hp}\n  MP: {current_mp}")
