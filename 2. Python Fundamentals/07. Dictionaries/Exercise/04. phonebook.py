input_list = input().split("-")
my_dictionary = {}
while len(input_list) > 1:
    name, phone_number = input_list[0], input_list[1]
    my_dictionary[name] = phone_number
    input_list = input().split("-")
numbers_looked = int(input_list[0])
for sequence in range(numbers_looked):
    name_looking = input()
    if name_looking in my_dictionary:
        print(f"{name_looking} -> {my_dictionary[name_looking]}")
    else:
        print(f"Contact {name_looking} does not exist.")
