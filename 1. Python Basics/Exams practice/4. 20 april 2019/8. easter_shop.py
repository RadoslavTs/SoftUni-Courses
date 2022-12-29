initial_egg_quantity = int(input())
trade = input()
sold_eggs = 0
break_flag = False
while trade != "Close":
    egg_transaction_quantity = int(input())
    if trade == "Buy":
        sold_eggs += egg_transaction_quantity
        initial_egg_quantity -= egg_transaction_quantity
    else:
        initial_egg_quantity += egg_transaction_quantity
    if initial_egg_quantity < 0:
        print("Not enough eggs in store!")
        eggs_remaining = initial_egg_quantity + egg_transaction_quantity
        print(f"You can buy only {eggs_remaining}.")
        break_flag = True
        break
    trade = input()
if not break_flag:
    print("Store is closed!")
    print(f"{sold_eggs} eggs sold.")
