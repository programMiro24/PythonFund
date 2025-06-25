class Zoo:
    __animals = 0
    __animals_list = ""

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        if species == 'mammal':
            Zoo.__animals_list = f"Mammals in {self.name}: {', '.join(self.mammals)}"
        elif species == 'fish':
            Zoo.__animals_list = f"Fishes in {self.name}: {', '.join(self.fishes)}"
        elif species == 'bird':
            Zoo.__animals_list = f"Birds in {self.name}: {', '.join(self.birds)}"

        Zoo.__animals_list += f"\nTotal animals: {Zoo.__animals}"
        return Zoo.__animals_list


name_of_zoo = input()
n = int(input())
zoo = Zoo(name_of_zoo)
for animal in range(n):
    species, animal_name = input().split()
    zoo.add_animal(species, animal_name)

species = input()
print(zoo.get_info(species))
