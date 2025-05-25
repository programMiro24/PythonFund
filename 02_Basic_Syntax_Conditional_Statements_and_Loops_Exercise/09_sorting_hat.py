name = input()

while name != "Welcome!":
    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    chars_on_name = len(name)
    if chars_on_name < 5:
        print(f"{name} goes to Gryffindor.")
    elif chars_on_name == 5:
        print(f"{name} goes to Slytherin.")
    elif chars_on_name == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")
    name = input()

if name == "Welcome!":
    print("Welcome to Hogwarts.")
