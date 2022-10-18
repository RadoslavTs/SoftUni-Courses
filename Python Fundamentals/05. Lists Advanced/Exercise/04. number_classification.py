input_list = list(map(int, input().split(", ")))
positive_list = [num for num in input_list if num >= 0]
negative_list = [num for num in input_list if num < 0]
even_list = [num for num in input_list if num % 2 == 0]
odd_list = [num for num in input_list if num % 2]
positive_list_str = list(map(str, positive_list))
negative_list_str = list(map(str, negative_list))
even_list_str = list(map(str, even_list))
odd_list_str = list(map(str, odd_list))
positive_string = "Positive: " + ", ".join(positive_list_str)
negative_string = "Negative: " + ", ".join(negative_list_str)
even_string = "Even: " + ", ".join(even_list_str)
odd_string = "Odd: " + ", ".join(odd_list_str)
print(positive_string)
print(negative_string)
print(even_string)
print(odd_string)
