input_list = input().split()
resulting_list = [word for word in input_list if len(word) % 2 == 0]
for word in resulting_list:
    print(word)
