name = input()
sorted_flag = True
while name != "Welcome!":
    if name == "Voldemort":
        print("You must not speak of that name!")
        sorted_flag = False
        break
    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")
    name = input()
if sorted_flag:
    print("Welcome to Hogwarts.")