pages = int(input())
page_rate = int(input())
time = int(input())
time_to_read = pages // page_rate
required_time = time_to_read / time
print(required_time)