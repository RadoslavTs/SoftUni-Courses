movie_name = input()
standard_tickets = 0
student_tickets = 0
kid_tickets = 0
seats_taken = 0
occupancy = 0
total_tickets_bought = 0
total_standard_tickets = 0
student_tickets_total = 0
kid_tickets_total = 0
while movie_name != "Finish":
    free_spaces = int(input())
    ticket_type = input()
    while ticket_type != "End":
        if ticket_type == "standard":
            standard_tickets += 1
            seats_taken += 1
            total_tickets_bought += 1
            total_standard_tickets += 1
        elif ticket_type == "student":
            student_tickets += 1
            seats_taken += 1
            total_tickets_bought += 1
            student_tickets_total += 1
        else:
            kid_tickets += 1
            seats_taken += 1
            total_tickets_bought += 1
            kid_tickets_total += 1
        if seats_taken == free_spaces:
            break
        ticket_type = input()
    occupancy = seats_taken / free_spaces * 100
    print(f"{movie_name} - {occupancy:.2f}% full.")
    occupancy = 0
    seats_taken = 0
    kid_tickets = 0
    student_tickets = 0
    standard_tickets = 0
    movie_name = input()
kids_percent = kid_tickets_total / total_tickets_bought * 100
standard_percent = total_standard_tickets / total_tickets_bought * 100
student_percent = student_tickets_total / total_tickets_bought * 100
print(f"Total tickets: {total_tickets_bought}")
print(f"{student_percent:.2f}% student tickets.")
print(f"{standard_percent:.2f}% standard tickets.")
print(f"{kids_percent:.2f}% kids tickets.")


