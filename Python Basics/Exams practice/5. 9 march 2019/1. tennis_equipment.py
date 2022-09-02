import math
cena_raketi = float(input())
broi_raketi = int(input())
broi_maratonki = int(input())
obshto_raketi = cena_raketi * broi_raketi
obshto_maratonki = cena_raketi / 6 * broi_maratonki
obshta_suma = obshto_raketi + obshto_maratonki
obshta_suma *= 1.2
suma_djokovic = obshta_suma / 8
suma_sponsori = obshta_suma - suma_djokovic
print(f"Price to be paid by Djokovic {math.floor(suma_djokovic):.0f}")
print(f"Price to be paid by sponsors {math.ceil(suma_sponsori):.0f}")