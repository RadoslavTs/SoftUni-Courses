def shopping_cart(*meals):
    meals_dict = {
        'Soup': [],
        'Pizza': [],
        'Dessert': []
    }

    limit_dict = {
        "Soup": 3,
        "Pizza": 4,
        "Dessert": 2
    }

    total_products = 0

    for meal in meals:
        if meal == "Stop":
            break
        current_meal = meal[0]
        current_product = meal[1]
        if current_product not in meals_dict[current_meal] and len(meals_dict[current_meal]) < limit_dict[current_meal]:
            meals_dict[current_meal].append(current_product)

    result = ''
    for meal, product in sorted(meals_dict.items(), key=lambda x: (-len(x[1]), x[0])):
        result += (f"{meal}:\n")
        for prod in sorted(product):
            result += f" - {prod}\n"

    for meal, product in meals_dict.items():
        total_products += len(product)

    if total_products:
        return result
    else:
        return f"No products in the cart!"


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

