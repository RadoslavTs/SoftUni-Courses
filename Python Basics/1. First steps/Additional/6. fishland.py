skumria_cena = float(input())
caca_cena = float(input())
palamud_cena = skumria_cena * 1.6
safrid_cena = caca_cena * 1.8
midi_cena = 7.5
palamud_kolichestvo = float(input())
safrid_kolichestvo = float(input())
midi_kolichestvo = float(input())
razhod_palamud = palamud_kolichestvo * palamud_cena
razhod_safrid = safrid_kolichestvo * safrid_cena
razhod_midi = midi_kolichestvo * midi_cena
total = razhod_palamud + razhod_safrid + razhod_midi
result="{:.2f}".format(total)
print(result)
