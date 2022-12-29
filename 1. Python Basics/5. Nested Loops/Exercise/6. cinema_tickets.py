movie_name = input()
standard_tickets_sold = 0
kid_tickets_sold = 0
student_tickets_sold = 0
total_tickets_sold = 0
total_tickets_all_time = 0
total_tickets_student = 0
total_tickets_standard = 0
total_tickets_kid = 0
while movie_name != "Finish":
    available_seats = int(input())
    for occupancy in range(available_seats):
        ticket_type = input()
        if ticket_type == "End":
            break
        if ticket_type == "standard":
            student_tickets_sold += 1
            total_tickets_sold +=1
            total_tickets_all_time += 1
            total_tickets_standard += 1
        elif ticket_type == "kid":
            kid_tickets_sold += 1
            total_tickets_sold +=1
            total_tickets_all_time += 1
            total_tickets_kid +=1
        else:
            student_tickets_sold += 1
            total_tickets_sold += 1
            total_tickets_all_time += 1
            total_tickets_student += 1
        occupied_cinema = total_tickets_sold / available_seats * 100
    print(f"{movie_name} - {occupied_cinema:.2f}% full.")
    kid_tickets_sold = 0
    student_tickets_sold = 0
    standard_tickets_sold = 0
    total_tickets_sold = 0
    movie_name = input()
student_perc = total_tickets_student / total_tickets_all_time * 100
standard_perc = total_tickets_standard / total_tickets_all_time * 100
kid_perc = total_tickets_kid / total_tickets_all_time * 100
print(f"Total tickets: {total_tickets_all_time}")
print(f"{student_perc:.2f}% student tickets.")
print(f"{standard_perc:.2f}% standard tickets.")
print(f"{kid_perc:.2f}% kids tickets.")