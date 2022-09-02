wrapping_paper_count = int(input())
fabric_count = int(input())
glue_liters = float(input())
discount = int(input())
discount /= 100
paper_cost = wrapping_paper_count * 5.8
fabric_cost = fabric_count * 7.2
glue_cost = glue_liters * 1.2
total_material_cost = paper_cost + fabric_cost + glue_cost
discount = total_material_cost * discount
final_cost = total_material_cost - discount
print(f"{final_cost:.3f}")