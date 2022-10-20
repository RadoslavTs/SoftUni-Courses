input_list = input().split()
resulting_list = [word for word in input_list if len(word) % 2 == 0]
print("\n".join(resulting_list))
