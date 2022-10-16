# def palindrome(number):
#     pali_list = []
#     for pali in number:
#         pali_check = "True"
#         if pali == pali[::-1]:
#             pass
#         else:
#             pali_check = "False"
#         pali_list.append(pali_check)
#     return pali_list
#
#
# entry_list = input().split(", ")
# result_list = palindrome(entry_list)
# print("\n".join(result_list))


list(map(lambda x: print(x == x[::-1]), input().split(", ")))
