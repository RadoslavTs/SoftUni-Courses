voucher_price = int(input())
product = input()
tickets_bought = 0
other_products_bought = 0
ticket_price = 0
while product != "End":
    if len(product) >= 8:
        ticket_price = ord(product[0]) + ord(product[1])
        if voucher_price >= ticket_price:
            voucher_price -= ticket_price
            tickets_bought += 1
            ticket_price = 0
        else:
            break
    else:
        ticket_price = ord(product[0])
        if voucher_price >= ticket_price:
            voucher_price -= ticket_price
            other_products_bought += 1
        else:
            break
    product = input()
print(f"{tickets_bought}")
print(f"{other_products_bought}")