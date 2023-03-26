def fibonacci():
    n1 = 0
    n2 = 1

    while True:
        yield n1
        n1, n2 = n2, n1 + n2


generator = fibonacci()
my_list = []
for i in range(5):
    print(next(generator))
# generator = fibonacci()
# for i in range(1):
#     print(next(generator))
