def forecast(*args):
    weather = {}
    for location in args:
        weather[location[0]] = location[1]

    sorted_weather = sorted(weather.items(), key=lambda x: (x[1], x[0]))

    sunny = ''
    cloudy = ''
    rainy = ''
    for city, forecats in sorted_weather:
        if forecats == "Sunny":
            sunny += f"{city} - {forecats}\n"
        elif forecats == "Cloudy":
            cloudy += f"{city} - {forecats}\n"
        elif forecats == "Rainy":
            rainy += f"{city} - {forecats}\n"

    return sunny + cloudy + rainy


print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
