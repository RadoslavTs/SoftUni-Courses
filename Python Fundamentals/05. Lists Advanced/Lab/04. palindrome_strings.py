input_list = input().split()
palindrome_searched = input()
palindrome_list = []
for sequence in range(len(input_list)):
    if input_list[sequence] == input_list[sequence][::-1]:
        palindrome_list.append(input_list[sequence])
print(palindrome_list)
palindrome_count = palindrome_list.count(palindrome_searched)
print(f"Found palindrome {palindrome_count} times")