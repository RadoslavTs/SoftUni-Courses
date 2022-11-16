input_text = input()
resulting_cipher = ""
for letter in input_text:
    resulting_cipher += chr(ord(letter)+3)
print(resulting_cipher)