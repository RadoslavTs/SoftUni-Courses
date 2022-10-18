first_list = input().split(", ")
second_list = input().split(", ")
check_string = "".join(second_list)
result_list = [word for word in first_list if word in check_string]
print(result_list)