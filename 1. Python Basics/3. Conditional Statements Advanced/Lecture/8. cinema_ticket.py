day = input()
ticket = int()
if day == "Monday" or day == "Tuesday" or day == "Friday":
    ticket = 12
elif day == "Wednesday" or day == "Thursday":
    ticket = 14
else:
    ticket = 16
print(ticket)