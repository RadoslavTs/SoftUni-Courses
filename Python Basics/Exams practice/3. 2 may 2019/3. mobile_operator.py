contract_length = input()
contract_type = input()
mobile_data = input()
months_to_pay = int(input())
monthly_tax = 0
if contract_length == "one":
    if contract_type == "Small":
        monthly_tax = 9.98
    elif contract_type == "Middle":
        monthly_tax = 18.99
    elif contract_type == "Large":
        monthly_tax = 25.98
    else:
        monthly_tax = 35.99
else:
    if contract_type == "Small":
        monthly_tax = 8.58
    elif contract_type == "Middle":
        monthly_tax = 17.09
    elif contract_type == "Large":
        monthly_tax = 23.59
    else:
        monthly_tax = 31.79
if mobile_data == "yes":
    if monthly_tax <= 10:
        monthly_tax += 5.5
    elif monthly_tax <= 30:
        monthly_tax += 4.35
    else:
        monthly_tax += 3.85
if contract_length == "two":
    monthly_tax *= 0.9625
sum_to_be_paid = monthly_tax * months_to_pay
print(f"{sum_to_be_paid:.2f} lv.")
