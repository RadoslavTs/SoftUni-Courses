temperature = int(input())
time_of_day = input()
outfit = str()
shoes = str()
if temperature >= 10 and temperature <= 18:
    if time_of_day == "Morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif time_of_day == "Afternoon":
        outfit = "Shirt"
        shoes = "Moccasins"
    else:
        outfit = "Shirt"
        shoes = "Moccasins"
elif temperature > 18 and temperature <= 24:
    if time_of_day == "Morning":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif time_of_day == "Afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"
    else:
        outfit = "Shirt"
        shoes = "Moccasins"
elif temperature >= 25:
    if time_of_day == "Morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif time_of_day == "Afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
    else:
        outfit = "Shirt"
        shoes = "Moccasins"
print(f"It's {temperature:.0f} degrees, get your {outfit} and {shoes}.")
