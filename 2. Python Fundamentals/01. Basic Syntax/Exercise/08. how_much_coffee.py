event = input()
one_coffee_events = ["coding", "dog", "cat", "movie"]
two_coffee_events = ["CODING", "DOG", "CAT", "MOVIE"]
coffee_needed = 0
need_sleep_flag = False
while event != "END":
    if event in one_coffee_events:
        coffee_needed += 1
    elif event in two_coffee_events:
        coffee_needed += 2
    if coffee_needed > 5:
        need_sleep_flag = True
    event = input()
if not need_sleep_flag:
    print(coffee_needed)
else:
    print("You need extra sleep")