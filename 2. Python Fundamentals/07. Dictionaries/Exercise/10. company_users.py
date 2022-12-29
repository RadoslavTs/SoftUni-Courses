input_list = input().split(" -> ")
my_dictionary = {}
while len(input_list) > 1:
    company, user_id = input_list[0], input_list[1]
    if company not in my_dictionary:
        my_dictionary[company] = []
    if user_id not in my_dictionary[company]:
        my_dictionary[company].append(user_id)
    input_list = input().split(" -> ")
for comp in my_dictionary:
    print(comp)
    for user in my_dictionary[comp]:
        print(f"-- {user}")
