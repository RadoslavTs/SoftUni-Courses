country = input()
type = input()
if country == "Russia":
    if type == "ribbon":
        hardness = 9.1
        performance = 9.4
    elif type == "hoop":
        hardness = 9.3
        performance = 9.8
    else:
        hardness = 9.6
        performance = 9
elif country == "Bulgaria":
    if type == "ribbon":
        hardness = 9.6
        performance = 9.4
    elif type == "hoop":
        hardness = 9.55
        performance = 9.75
    else:
        hardness = 9.5
        performance = 9.4
else:
    if type == "ribbon":
        hardness = 9.2
        performance = 9.5
    elif type == "hoop":
        hardness = 9.45
        performance = 9.35
    else:
        hardness = 9.7
        performance = 9.150
score = hardness + performance
remain = (20 - score) / 20 * 100
print(f"The team of {country} get {score:.3f} on {type}.")
print(f"{remain:.2f}%")