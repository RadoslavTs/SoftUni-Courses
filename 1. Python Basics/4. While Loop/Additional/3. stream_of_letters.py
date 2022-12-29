import string
letter = input()
correct_list = string.ascii_lowercase + string.ascii_uppercase
secret_n = False
secret_o = False
secret_c = False
resulting_string = str()
temp_string = ""
while letter != "End":
    if letter in correct_list:
        if letter == "n" and secret_n:
            temp_string += letter
        elif letter == "o" and secret_o:
            temp_string += letter
        elif letter == "c" and secret_c:
            temp_string += letter
        elif letter != "n" and letter != "o" and letter != "c":
            temp_string += letter
    if letter == "n":
        secret_n = True
    elif letter == "o":
        secret_o = True
    elif letter == "c":
        secret_c = True
    if secret_n and secret_o and secret_c:
        secret_n = False
        secret_o = False
        secret_c = False
        resulting_string += temp_string
        resulting_string += " "
        temp_string = ""
    letter = input()
print(resulting_string)

