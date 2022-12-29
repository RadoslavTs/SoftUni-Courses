kozunak_count = int(input())
eggs_count = int(input())
cookies_kg = float(input())
kozunak_cost = kozunak_count * 3.2
eggs_cost = 4.35 * eggs_count
cookies_cost = 5.4 * cookies_kg
egg_paint = eggs_count * 12 * 0.15
total_cost = kozunak_cost + eggs_cost + cookies_cost + egg_paint
print(f"{total_cost:.2f}")
