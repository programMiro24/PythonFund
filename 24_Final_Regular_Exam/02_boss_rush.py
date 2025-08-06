import re

number_of_bosses = int(input())
pattern = r'(\|)([A-Z]{4,})\1(:)(#)([A-z]*\s[A-z]*)\4'

for number_of_boss in range(number_of_bosses):
    boss_information = input()
    if re.match(pattern, boss_information):
        information_about_matches = re.match(pattern, boss_information).groups()
        boss_name = information_about_matches[1]
        title = information_about_matches[4]
        strength = len(boss_name)
        armor = len(title)
        print(f"{boss_name}, The {title}\n>> Strength: {strength}\n>> Armor: {armor}")
    else:
        print("Access denied!")
