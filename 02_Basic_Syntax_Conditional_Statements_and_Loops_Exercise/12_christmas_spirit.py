# consts
ORNAMENT_SET_PRICE = 2
ORNAMENT_SET_POINTS = 5
TREE_SKIRT_PRICE = 5
TREE_SKIRT_POINTS = 3
TREE_GARLAND_PRICE = 3
TREE_GARLAND_POINTS = 10
TREE_LIGHTS_PRICE = 15
TREE_LIGHTS_POINTS = 17
BONUS_POINTS = 30
CAT_POINTS = 20
LOST_POINTS = 30
# input
quantity_of_decorations = int(input())
remaining_days = int(input())
# variables for total cost and spirit points
total_cost = 0
total_spirit = 0
# for remaining days
for current_day in range(1, remaining_days+1):
    if current_day % 11 == 0:
        quantity_of_decorations += 2
    if current_day % 2 == 0:
        total_cost += (ORNAMENT_SET_PRICE * quantity_of_decorations)
        total_spirit += ORNAMENT_SET_POINTS
    if current_day % 3 == 0:
        total_cost += (TREE_SKIRT_PRICE + TREE_GARLAND_PRICE) * quantity_of_decorations
        total_spirit += (TREE_SKIRT_POINTS + TREE_GARLAND_POINTS)
    if current_day % 5 == 0:
        total_cost += (TREE_LIGHTS_PRICE * quantity_of_decorations)
        total_spirit += TREE_LIGHTS_POINTS
        if current_day % 3 == 0:
            total_spirit += BONUS_POINTS
    if current_day % 10 == 0:
        total_spirit -= CAT_POINTS
        total_cost += TREE_SKIRT_PRICE + TREE_LIGHTS_PRICE + TREE_GARLAND_PRICE
if remaining_days % 10 == 0:
    total_spirit -= LOST_POINTS
print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
