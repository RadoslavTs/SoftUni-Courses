width = int(input())
length = int(input())
pieces = width * length
stop_command = False
while pieces > 0:
    pieces_taken = input()
    if pieces_taken == "STOP":
        stop_command = True
        break
    pieces -= int(pieces_taken)
if stop_command:
    print(f"{pieces} pieces are left.")
else:
    print(f"No more cake left! You need {abs(pieces)} pieces more.")

