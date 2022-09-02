budget = float(input())
product = input()
counter = 0
total_cost = 0
overrun_flag = False
while product != "Stop":
    product_price = float(input())
    counter += 1
    if counter % 3 == 0:
        product_price /= 2
    total_cost += product_price
    if budget < total_cost:
        overrun_flag = True
        break
    product_price = 0
    product = input()
difference = abs(budget - total_cost)
if product == "Stop" and not overrun_flag:
    print(f"You bought {counter} products for {total_cost:.2f} leva.")
elif overrun_flag:
    print("You don't have enough money!")
    print(f"You need {difference:.2f} leva!")
