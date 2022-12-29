number = int(input())
prime_flag = True
if number == 0 or number == 1:
    prime_flag = True
else:
    for check in range(2, number):
        if number % check == 0:
            prime_flag = False
            break
print(prime_flag)