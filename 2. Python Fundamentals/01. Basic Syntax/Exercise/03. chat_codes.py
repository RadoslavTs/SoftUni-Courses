number_of_messages = int(input())
for _ in range(number_of_messages):
    code_number = int(input())
    if code_number == 88:
        print("Hello")
    elif code_number == 86:
        print("How are you?")
    elif code_number < 88:
        print("GREAT!")
    else:
        print("Bye.")