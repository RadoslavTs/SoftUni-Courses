try:
    input_string = input()
    repeat_times = int(input())
    print(input_string * repeat_times)

except ValueError:
    print("Variable times must be an integer")
