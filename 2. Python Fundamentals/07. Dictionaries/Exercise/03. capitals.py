# countries = input().split(", ")
# capitals = input().split(", ")
# my_dictionary = {}
# for country in countries:
#     index_capital = countries.index(country)
#     my_dictionary[country] = capitals[index_capital]
# for key, value in my_dictionary.items():
#     print(f"{key} -> {value}")

countries = input().split(", ")
capitals = input().split(", ")
# my_dictionary = {countries[index]: capitals[index] for index in range(len(capitals))}
my_dictionary = dict(zip(countries, capitals))
for country, capital in my_dictionary.items():
    print(f"{country} -> {capital}")
