#consts
LOWERCASE_COFFEES = 1
UPPERCASE_COFFEES = 2
event = input()
number_of_coffees = 0
while event != "END":
    if event.lower() == "cat"\
            or event.lower() == "dog"\
            or event.lower() == "coding"\
            or event.lower() == "movie":
        if event.lower() == event:
            number_of_coffees += LOWERCASE_COFFEES
        else:
            number_of_coffees += UPPERCASE_COFFEES
    event = input()

if number_of_coffees <= 5:
    print(number_of_coffees)
else:
    print("You need extra sleep")