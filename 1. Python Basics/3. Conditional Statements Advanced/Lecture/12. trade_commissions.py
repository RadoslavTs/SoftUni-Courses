city = input()
sales = float(input())
commision = float()
if city == "Sofia" and sales >= 0:
    if sales >= 0 and sales <= 500:
        commision = sales * 0.05
    elif sales > 500 and sales <= 1000:
        commision = sales * 0.07
    elif sales > 1000 and sales <= 10000:
        commision = sales * 0.08
    else:
        commision = sales * 0.12
elif city == "Varna" and sales >= 0:
    if sales >= 0 and sales <= 500:
        commision = sales * 0.045
    elif sales > 500 and sales <= 1000:
        commision = sales * 0.075
    elif sales > 1000 and sales <= 10000:
        commision = sales * 0.1
    else:
        commision = sales * 0.13
elif city == "Plovdiv" and sales >= 0:
    if sales >= 0 and sales <= 500:
        commision = sales * 0.055
    elif sales > 500 and sales <= 1000:
        commision = sales * 0.08
    elif sales > 1000 and sales <= 10000:
        commision = sales * 0.12
    else:
        commision = sales * 0.145
else:
    commision = 0
if commision > 0:
    print(f"{commision:.2f}")
else:
    print("error")