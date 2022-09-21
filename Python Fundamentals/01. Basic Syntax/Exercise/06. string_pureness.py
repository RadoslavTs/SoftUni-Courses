# number = int(input())
# string_pureness_flag = True
# for sequence in range(number):
#     string_name = input()
#     for sequence_two in range(len(string_name)):
#         if string_name[sequence_two] == "," or string_name[sequence_two] == "." or string_name[sequence_two] == "_":
#             string_pureness_flag = False
#     if not string_pureness_flag:
#         print(f"{string_name} is not pure!")
#     else:
#         print(f"{string_name} is pure.")

# number = int(input())
# string_pureness_flag = True
# for sequence in range(number):
#     string_name = input()
#     if "." in string_name or "," in string_name or "_" in string_name:
#         print(f"{string_name} is not pure!")
#     else:
#         print(f"{string_name} is pure.")

number = int(input())
banned = [",", ".", "_"]
pure = True
for sequence in range(number):
    current_string = input()
    for letter in banned:
        if letter in current_string:
            pure = False
            break
    if pure:
        print(f"{current_string} is pure.")
    else:
        print(f"{current_string} is not pure!")
    pure = True