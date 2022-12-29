import math
yard_area = int(input())
grapes_quantity_per_sq_m = float(input())
needed_wine_liters = int(input())
quantity_workers = int(input())
grapes_produced = yard_area * 0.4 * grapes_quantity_per_sq_m
wine_produced = grapes_produced / 2.5
missing_wine = needed_wine_liters - wine_produced
extra_wine = wine_produced - needed_wine_liters
wine_per_worker = extra_wine / quantity_workers
if wine_produced < needed_wine_liters:
    print(f"It will be a tough winter! More {math.floor(missing_wine)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {math.floor(wine_produced)} liters.")
    print(f"{math.ceil(extra_wine)} liters left -> {math.ceil(wine_per_worker)} liters per person.")