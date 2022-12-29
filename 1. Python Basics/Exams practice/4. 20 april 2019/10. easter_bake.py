from math import ceil
konunak_count = int(input())
total_sugar_used = int()
total_flour_used = int()
max_sugar = int()
max_flour = int()

for sequence in range(konunak_count):
    sugar_used = int(input())
    flour_used = int(input())
    if sugar_used > max_sugar:
        max_sugar = sugar_used
    if flour_used > max_flour:
        max_flour = flour_used
    total_sugar_used += sugar_used
    total_flour_used += flour_used
total_packs_sugar_needed = total_sugar_used / 950
total_packs_flour_needed = total_flour_used / 750
print(f"Sugar: {ceil(total_packs_sugar_needed)}")
print(f"Flour: {ceil(total_packs_flour_needed)}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")

