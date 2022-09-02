# hours = int()
# minutes = int()
# seconds = int()
# for hour in range(24):
#     for minute in range(60):
#         for second in range(60):
#             if second < 10 and minute < 10 and hour < 10:
#                 print(f"0{hour} : 0{minute} : 0{second}")
#             elif second < 10 and minute > 10 and hour > 10:
#                 print(f"{hour} : {minute} : 0{second}")
#             elif second > 10 and minute < 10 and hour > 10:
#                 print(f"{hour} : 0{minute} : {second}")
#             elif second > 10 and minute > 10 and hour < 10:
#                 print(f"0{hour} : {minute} : {second}")
#             elif second < 10 and minute < 10 and hour > 10:
#                 print(f"{hour} : 0{minute} : 0{second}")
#             elif second < 10 and minute > 10 and hour < 10:
#                 print(f"0{hour} : {minute} : 0{second}")
#             elif second > 10 and minute < 10 and hour < 10:
#                 print(f"0{hour} : 0{minute} : {second}")

for hour in range(24):
    for minute in range(60):
        for second in range(60):
            hour_str = hour if hour > 9 else f"0{hour}"
            minute_str = minute if minute > 9 else f"0{minute}"
            second_str = second if second > 9 else f"0{second}"
            print(f"{hour_str} : {minute_str} : {second_str}")