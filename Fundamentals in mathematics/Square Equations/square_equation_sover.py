import math
a = float(input("Въведете първи член: "))
b = float(input("Въведете втори член: "))
c = float(input("Въведете трети член: "))
if a != 0:
    descr = int((b * b) - (4 * a * c))
    if descr > 0:
        print(f"Дескреминантата е: {descr} и уравнението има два реални корена")
        x1 = (-b - math.sqrt(descr)) / (2 * a)
        x2 = (-b + math.sqrt(descr)) / (2 * a)
        print(f"първият корен x1 = {x1:.2f}")
        print(f"вторият корен x2 = {x2:.2f}")
    elif descr == 0:
        print(f"Дескреминантата е: {descr} и уравнението има един реален корен")
        x = -b / (2 * a)
        print(f"коренът на уравнението x = {x:.2f}")
    else:
        print(f"Дескреминантата е: {descr} и уравнението няма реални корени")
else:
    print("първият член не може да е 0!")

