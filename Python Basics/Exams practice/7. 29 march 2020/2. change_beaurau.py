bitcoin_count = int(input())
chinese_count = float(input())
commision = float(input())
commision = commision / 100
bitcoin_lv = bitcoin_count * 1168
chinese_usd = chinese_count * 0.15
chinese_bgn = chinese_usd *1.76
bitcoin_eur = bitcoin_lv / 1.95
chinese_eur = chinese_bgn / 1.95
total_currency_eur = bitcoin_eur + chinese_eur
commision_cost = commision * total_currency_eur
total = total_currency_eur - commision_cost
result = "{:.2f}".format(total)
print(result)
