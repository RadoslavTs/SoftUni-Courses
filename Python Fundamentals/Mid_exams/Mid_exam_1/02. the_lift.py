waiting_people = int(input())
remaining_people = waiting_people
current_state = input().split()
final_state = current_state
final_state_string = ""
for sequence in range(len(current_state)):
    available_spaces_current_wagon = 4 - int(current_state[sequence])
    occupied_spaces = 4 - available_spaces_current_wagon
    if remaining_people < available_spaces_current_wagon:
        final_state[sequence] = remaining_people
        remaining_people = 0
    else:
        final_state[sequence] = available_spaces_current_wagon + occupied_spaces
        remaining_people -= available_spaces_current_wagon
for element in final_state:
    final_state_string += str(element) + " "
if final_state[-1] < 4:
    print("The lift has empty spots!")
    print(final_state_string)
else:
    print(f"There isn't enough space! {remaining_people} people in a queue!")
    print(final_state_string)