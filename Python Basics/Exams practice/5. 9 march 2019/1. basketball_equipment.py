yearly_tax = float(input())
kecove = yearly_tax * 0.6
ekip = kecove * 0.8
topka = ekip / 4
accessories = topka / 5
total = yearly_tax + kecove + ekip + topka + accessories
print(f"{total:.2f}")