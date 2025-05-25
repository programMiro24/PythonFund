# const
KIDS_MAXIMUM_AGE = 14
TEENS_MAXIMUM_AGE = 18
YOUNG_ADULTS_MAXIMUM_AGE = 21
ADULT_MINIMUM_AGE = 21
KIDS_DRINK = "toddy"
TEENS_DRINK = "coke"
YOUNG_ADULTS_DRINK = "beer"
ADULTS_DRINK = "whisky"
age = int(input())  # age
drink = ""  # drink for the person
# if - elif - else
if age <= KIDS_MAXIMUM_AGE:  # kids
    drink = KIDS_DRINK
elif age <= TEENS_MAXIMUM_AGE:  # teens
    drink = TEENS_DRINK
elif age <= YOUNG_ADULTS_MAXIMUM_AGE:  # young_adults
    drink = YOUNG_ADULTS_DRINK
else:  # adult
    drink = ADULTS_DRINK
print(f"drink {drink}")
