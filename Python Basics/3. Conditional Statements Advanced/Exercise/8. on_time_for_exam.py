exam_hour = int(input()) #час на изпита
exam_min = int(input()) #минути на изпита
arrival_hour = int(input()) #час на пристигане
arrival_minute = int(input()) #минути на пристигане
exam_all_min = (exam_hour * 60) + exam_min #общо минути на изпита
arrival_all_min = (arrival_hour * 60) + arrival_minute #общо минути на пристигане
difference = abs(exam_all_min - arrival_all_min) #разлика
hour = difference // 60
min = difference % 60
difference_two = arrival_all_min - exam_all_min
difference_hours = difference // 60
difference_minutes = difference % 60
difference_two_hours = difference_two // 60
difference_two_minutes = difference_two % 60
if arrival_all_min > exam_all_min: #Late условие
    print("Late")
    if difference < 60:
        print(f"{(difference)} minutes after the start")
    else:
        if difference_minutes < 10:
            print(f"{hour}:0{min} hours after the start")
        else:
            print(f"{hour}:{min} hours after the start")
elif arrival_all_min == exam_all_min or difference <= 30:
    if arrival_all_min == exam_all_min:
        print("On time")
    elif arrival_all_min <= exam_all_min and exam_all_min - arrival_all_min <= 30:
        print("On time")
        print(f"{difference} minutes before the start")
else:
    if exam_all_min - arrival_all_min < 60:
        print("Early")
        print(f"{(exam_all_min - arrival_all_min)} minutes before the start")
    elif exam_all_min - arrival_all_min >= 60:
        if difference_minutes < 10:
            print("Early")
            print(f"{hour}:0{min} hours before the start")
        else:
            print("Early")
            print(f"{hour}:{min} hours before the start")