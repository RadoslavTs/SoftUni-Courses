budget = float(input())
season = input()
type_of_accomodation = str()
location = str()
cost = float()
if budget <= 1000:
    type_of_accomodation = "Camp"
    if season == "Summer":
        location = "Alaska"
        cost = budget * 0.65
    else:
        location = "Morocco"
        cost = budget * 0.45
elif budget > 1000 and budget <= 3000:
    type_of_accomodation = "Hut"
    if season == "Summer":
        location = "Alaska"
        cost = budget * 0.8
    else:
        location = "Morocco"
        cost = budget * 0.6
else:
    type_of_accomodation = "Hotel"
    cost = budget * 0.9
    if season == "Summer":
        location = "Alaska"
    else:
        location = "Morocco"
print(f"{location} - {type_of_accomodation} - {cost:.2f}")