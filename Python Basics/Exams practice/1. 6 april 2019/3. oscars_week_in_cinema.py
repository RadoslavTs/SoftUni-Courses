movie_name = input()
theatre_type = input()
tickets_bought = int(input())
total_income = 0
if movie_name == "A Star Is Born":
    if theatre_type == "normal":
        total_income = tickets_bought * 7.5
    elif theatre_type == "luxury":
        total_income = tickets_bought * 10.5
    else:
        total_income = tickets_bought * 13.5
if movie_name == "Bohemian Rhapsody":
    if theatre_type == "normal":
        total_income = tickets_bought * 7.35
    elif theatre_type == "luxury":
        total_income = tickets_bought * 9.45
    else:
        total_income = tickets_bought * 12.75
if movie_name == "Green Book":
    if theatre_type == "normal":
        total_income = tickets_bought * 8.15
    elif theatre_type == "luxury":
        total_income = tickets_bought * 10.25
    else:
        total_income = tickets_bought * 13.25
if movie_name == "The Favourite":
    if theatre_type == "normal":
        total_income = tickets_bought * 8.75
    elif theatre_type == "luxury":
        total_income = tickets_bought * 11.55
    else:
        total_income = tickets_bought * 13.95
print(f"{movie_name} -> {total_income:.2f} lv.")