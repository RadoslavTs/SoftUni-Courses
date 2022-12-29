age = input()
adults = 0
kids = 0
money_for_toys = 0
money_for_sweeters = 0
while age != "Christmas":
    age = int(age)
    if age <= 16:
        kids += 1
    else:
        adults += 1
    age = input()
money_for_toys = kids * 5
money_for_sweeters = adults * 15
print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {money_for_toys:.0f}")
print(f"Money for sweaters: {money_for_sweeters:.0f}")
