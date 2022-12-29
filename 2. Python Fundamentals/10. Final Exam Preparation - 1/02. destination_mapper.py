import re

locations = input()
pattern = r'([=/])([A-Z][A-Za-z]{2,})\1'

destinations = re.finditer(pattern, locations)
final_destination = []

for destination in destinations:
    final_destination.append(destination.group(2))
total_travel_points = 0
for travel_point in final_destination:
    total_travel_points += len(travel_point)
itterary = ", ".join(final_destination)
print(f"Destinations: {itterary}")
print(f"Travel Points: {total_travel_points}")
