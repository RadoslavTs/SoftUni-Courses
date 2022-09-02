days_count = int(input())
food_quantity = float(input())
biscuits_eaten = float()
total_dog_food = float()
total_cat_food = float()
total_food_eaten = float()
for sequence in range(1,days_count + 1):
    dog_eaten_food = float(input())
    cat_eaten_food = float(input())
    if sequence % 3 == 0:
        biscuits = (dog_eaten_food + cat_eaten_food) * 0.1
        biscuits_eaten += biscuits
    total_cat_food += cat_eaten_food
    total_dog_food += dog_eaten_food
    total_food_eaten += dog_eaten_food + cat_eaten_food
print(f"Total eaten biscuits: {round(biscuits_eaten)}gr.")
print(f"{((total_dog_food + total_cat_food) / food_quantity * 100):.2f}% of the food has been eaten.")
print(f"{(total_dog_food / total_food_eaten * 100):.2f}% eaten from the dog.")
print(f"{(total_cat_food / total_food_eaten * 100):.2f}% eaten from the cat.")

