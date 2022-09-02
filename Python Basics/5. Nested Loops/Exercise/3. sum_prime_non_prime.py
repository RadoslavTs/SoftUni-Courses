sum_primes = 0
sum_non_primes = 0
number = input()

while number != "stop":
    prime_flag = True
    number = int(number)
    if number < 0:
        print("Number is negative.")
        number = 0
    if number == 0 or number == 1:
        sum_primes += number
    for check in range(2, number):
        if number % check == 0:
            sum_non_primes += number
            prime_flag = False
            break
    if prime_flag:
        sum_primes += number

    number = input()
print(f"Sum of all prime numbers is: {sum_primes}")
print(f"Sum of all non prime numbers is: {sum_non_primes}")