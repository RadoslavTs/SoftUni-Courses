himikali = int(input())
cena_himikali = himikali * 5.8
markeri = int(input())
cena_markeri = markeri * 7.2
preparat = int(input())
cena_preparat = preparat * 1.2
discount = int(input())
suma = cena_himikali + cena_markeri + cena_preparat
suma_discount = suma * discount / 100
total = suma - suma_discount
print(total)