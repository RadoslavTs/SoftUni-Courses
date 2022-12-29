kvadratura = int(input())
paint_quantity = int(input())
dilutant_quantity = int(input())
needed_hours = int(input())
nylon_price = kvadratura * 1.5
paint_price = paint_quantity * 14.5
dilutant_price = dilutant_quantity * 5
final_paint_price = paint_price + paint_price * 0.1
final_nylon_price = nylon_price + 3
torbichki = 0.4
total_material_cost = torbichki + final_nylon_price + final_paint_price + dilutant_price
labor_cost = total_material_cost * 0.3 * needed_hours
total_cost = total_material_cost + labor_cost
print(total_cost)
