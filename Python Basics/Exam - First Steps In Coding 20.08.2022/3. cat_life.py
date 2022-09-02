cat_breed = input()
cat_sex = input()
life_expectancy = 0
invalid_cat_flag = False
if cat_sex == "m":
    if cat_breed == "British Shorthair":
        life_expectancy = 13
    elif cat_breed == "Siamese":
        life_expectancy = 15
    elif cat_breed == "Persian":
        life_expectancy = 14
    elif cat_breed == "Ragdoll":
        life_expectancy = 16
    elif cat_breed == "American Shorthair":
        life_expectancy = 12
    elif cat_breed == "Siberian":
        life_expectancy = 11
    else:
        invalid_cat_flag = True
else:
    if cat_breed == "British Shorthair":
        life_expectancy = 14
    elif cat_breed == "Siamese":
        life_expectancy = 16
    elif cat_breed == "Persian":
        life_expectancy = 15
    elif cat_breed == "Ragdoll":
        life_expectancy = 17
    elif cat_breed == "American Shorthair":
        life_expectancy = 13
    elif cat_breed == "Siberian":
        life_expectancy = 12
    else:
        invalid_cat_flag = True
human_months = life_expectancy * 12
cat_months = human_months / 6
if invalid_cat_flag:
    print(f"{cat_breed} is invalid cat!")
else:
    print(f"{cat_months:.0f} cat months")