PERCENT_FOR_PRICE_FOR_ONE_PACK_EGGS = 0.75
PERCENT_FOR_PRICE_FOR_ONE_L_MILK = 0.25

budget = float(input())
price_for_one_kg_floor = float(input())

number_of_loaves = 0
colored_eggs = 0
eggs_now = 3

price_for_egg_pack = PERCENT_FOR_PRICE_FOR_ONE_PACK_EGGS * price_for_one_kg_floor
price_for_milk_for_bread = (price_for_one_kg_floor +
                            (price_for_one_kg_floor * PERCENT_FOR_PRICE_FOR_ONE_L_MILK))/4
while True:
    if budget < (price_for_egg_pack + price_for_milk_for_bread + price_for_one_kg_floor):
        break
    number_of_loaves += 1
    if number_of_loaves % 3 == 0:
        colored_eggs -= (number_of_loaves - 2)
    colored_eggs += 3
    budget -= (price_for_egg_pack + price_for_milk_for_bread + price_for_one_kg_floor)

print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
