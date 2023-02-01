from collections import deque

seats = input().split(', ')
sequence_one = deque(list(map(int, input().split(', '))))
sequence_two = deque(list(map(int, input().split(', '))))
taken_seats = []
rotations = 0

while len(taken_seats) < 3 and rotations < 10:
    first_sequence_num = sequence_one.popleft()
    second_sequence_num = sequence_two.pop()
    current_sum = first_sequence_num + second_sequence_num
    ascii_sum = chr(current_sum)
    first_seat_check = str(first_sequence_num) + ascii_sum
    second_seat_check = str(second_sequence_num) + ascii_sum
    rotations += 1
    if first_seat_check in taken_seats or second_seat_check in taken_seats:
        continue
    elif first_seat_check in seats:
        seats.remove(first_seat_check)
        taken_seats.append(first_seat_check)
    elif second_seat_check in seats:
        seats.remove(second_seat_check)
        taken_seats.append(second_seat_check)
    else:
        sequence_one.append(first_sequence_num)
        sequence_two.appendleft(second_sequence_num)


seats_result = ''
for seat in taken_seats:
    seats_result += seat + ', '

print(f"Seat matches: {seats_result[:-2]}")
print(f"Rotations count: {rotations}")