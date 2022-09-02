open_tabs = int(input())
website = str()
salary = float(input())
accumulated_fine = float()
for sequence in range(open_tabs):
    website = input()
    if website == "Facebook":
        salary = salary - 150
        if salary <= 0:
            print("You have lost your salary.")
            break
    elif website == "Instagram":
        salary = salary - 100
        if salary <= 0:
            print("You have lost your salary.")
            break
    elif website == "Reddit":
        salary = salary - 50
        if salary <= 0:
            print("You have lost your salary.")
            break
    else:
        pass
if salary > 0:
    print(f"{salary:.0f}")