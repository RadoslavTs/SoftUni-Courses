key_input = list(map(int, input().split()))
command = input()
last_key_index = 0
while command != "find":
    decrypted_message = ""
    for character in command:
        searched_character = chr(ord(character) - key_input[last_key_index])
        decrypted_message += searched_character
        last_key_index += 1
        if last_key_index == len(key_input):
            last_key_index = 0
    last_key_index = 0
    treasure = decrypted_message.split("&")[-2]
    location = decrypted_message.split("<")[-1][:-1]
    print(f"Found {treasure} at {location}")
    command = input()
