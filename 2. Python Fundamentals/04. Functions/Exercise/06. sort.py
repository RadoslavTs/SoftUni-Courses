def sort_func(some_list):
    return sorted(some_list)


input_list = input().split()
integer_list = list(map(int, input_list))
print(sort_func(integer_list))

# sorted_numbers = list(sorted(input().split()))
# print(sorted_numbers)
# sorted_numbers_int = list(map(int, sorted_numbers))
# print(sorted_numbers_int)