key = int(input())
number_of_lines = int(input())
decrypted_message = ""
resulting_letter = ""
for sequence in range(number_of_lines):
    letter = input()
    decrypted_message += chr(ord(letter) + key)
print(decrypted_message)
