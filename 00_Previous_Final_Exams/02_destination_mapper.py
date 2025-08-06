import re

places = input()
pattern = r'(=|\/)([A-Z][a-zA-Z]{2,})\1'
matches = re.findall(pattern, places)

destinations = []

for match in matches:
    destination = match[1]
    destinations.append(destination)

travel_points = sum((len(destination) for destination in destinations))

print(f"Destinations: {', '.join(destinations)}")
print(f'Travel Points: {travel_points}')
