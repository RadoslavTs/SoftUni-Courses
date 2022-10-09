def perfect(x):
    current_sum = 0
    for sequence in range(1, int(x)):
        if int(x) % sequence == 0:
            current_sum += sequence
    if current_sum == int(x):
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


perfect(input())
