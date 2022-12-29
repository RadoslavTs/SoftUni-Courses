budget = int(input())
product = input()
while product != "End":
    product = int(product)
    if budget < product:
        print("You went in overdraft!")
        break
    else:
        budget -= product
    product = input()
if product == "End":
    print("You bought everything needed.")
