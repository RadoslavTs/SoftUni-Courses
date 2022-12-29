cena_zelen = float(input())
cena_plodove = float(input())
broi_zelen = int(input())
broi_plodove = int(input())
suma_zelen = cena_zelen * broi_zelen
suma_plodove = cena_plodove * broi_plodove
suma_leva = suma_zelen + suma_plodove
suma_eur = suma_leva / 1.94
result = "{:.2f}".format(suma_eur)
print(result)