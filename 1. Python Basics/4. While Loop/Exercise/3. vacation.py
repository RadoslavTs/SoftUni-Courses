# needed_money = float(input())
# owned_money = float(input())
# day_counter = 0
# spending_counter = 0
# while needed_money > owned_money and spending_counter < 5:
#     action = input()
#     money = input()
#     day_counter += 1
#     if action == "save":
#         owned_money += float(money)
#         spending_counter = 0
#     else:
#         owned_money -= float(money)
#         spending_counter += 1
#     if owned_money < 0:
#         owned_money = 0
# if spending_counter == 5:
#     print("You can't save the money.")
#     print(f"{day_counter}")
# else:
#     print(f"You saved the money for {day_counter} days.")

needed_money = float(input())
money_owned = float(input())
spending_counter = 0
spending_flag = False
days = 0
while money_owned < needed_money and not spending_flag:
    action = input()
    current_sum = float(input())
    if action == "spend":
        money_owned -= current_sum
        if money_owned < 0:
            money_owned = 0
        spending_counter += 1
        if spending_counter == 5:
            spending_flag = True
    else:
        money_owned += current_sum
        spending_counter = 0
    days += 1
if spending_flag:
    print("Yoy can't save the money!")
    print(days)
else:
    print(f"You saved the money for {days} days.")
