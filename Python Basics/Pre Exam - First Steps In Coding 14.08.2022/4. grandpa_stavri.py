days_count = int(input())
total_rakia = 0
strength_sum = 0
for sequence in range(days_count):
    rakia_quantity = float(input())
    rakia_strength = float(input())
    total_rakia += rakia_quantity
    strength_sum += (rakia_quantity * rakia_strength)
total_strength = strength_sum / total_rakia
print(f"Liter: {total_rakia:.2f}")
print(f"Degrees: {total_strength:.2f}")
if total_strength < 38:
    print("Not good, you should baking!")
elif total_strength <= 42 and total_strength >= 38:
    print("Super!")
elif total_strength > 42:
    print("Dilution with distilled water!")