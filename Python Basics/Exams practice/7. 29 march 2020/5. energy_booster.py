fruit = str(input())
if fruit == "Watermelon":
    fruit = "Watermelon"
elif fruit == "Mango":
    fruit = "Mango"
elif fruit == "Pineapple":
    fruit = "Pineapple"
elif fruit == "Raspberry":
    fruit = "Raspberry"
else:
    print("wrong input")
size = str(input())
if size == "small":
    size = "small"
elif size == "big":
    size = "big"
else:
    print("wrong input")
number_sets = int(input())
cost = float()
discount = float()
if fruit == "Watermelon" and size == "small":
    cost = 56 * number_sets * 2
elif fruit == "Watermelon" and size == "big":
    cost = 28.7 * number_sets * 5
elif fruit == "Mango" and size == "small":
    cost = 36.66 * number_sets * 2
elif fruit == "Mango" and size == "big":
    cost = 19.6 * number_sets * 5
elif fruit == "Pineapple" and size == "small":
    cost = 42.10 * number_sets * 2
elif fruit == "Pineapple" and size == "big":
    cost = 24.8 * number_sets * 5
elif fruit == "Raspberry" and size == "small":
    cost = 20 * number_sets * 2
elif fruit == "Raspberry" and size == "big":
    cost = 15.2 * number_sets * 5
if cost >= 400 and cost <= 1000:
    discount = cost * 0.15
elif cost > 1000:
    discount = cost * 0.5
cost_with_discount = cost - discount
cost_with_discount_result = "{:.2f}".format(cost_with_discount)
print(f"{cost_with_discount_result} lv.")
