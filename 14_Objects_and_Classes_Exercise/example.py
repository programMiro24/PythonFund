class People:
    number_of_people = 0
    bad_people = []

    def __init__(self, name: str, number_of_people: int,
                 floor: int, apartment_number: int):
        self.name = name
        self.number_of_people = number_of_people
        self.floor = floor
        self.apartment_number = apartment_number
        self._protected_attr = 0
        self.__private_attr = "Petrovi"

    def __repr__(self):
        return f"My name is {self.name}, i'm living on the {self.floor}, "\
            f"my ap. number is {self.apartment_number}"


family_one = People(name="Georgievi", number_of_people=4, floor=5, apartment_number=16)
family_two = People(name="Petrovi", number_of_people=4, floor=7, apartment_number=19)
print(family_one)
print(family_two)
