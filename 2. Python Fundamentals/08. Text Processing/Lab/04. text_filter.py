input_list = input().split(", ")
text_string = input()
for word in input_list:
    text_string = text_string.replace(word, "*" * len(word))
# for sequence in range(len(input_list)):
#     while input_list[sequence] in text_string:
#         text_string = text_string.replace(input_list[sequence], f"{len(input_list[sequence]) * '*'}")
print(text_string)
