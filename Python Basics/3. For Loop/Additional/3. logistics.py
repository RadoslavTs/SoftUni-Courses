cargos = int(input())
price_per_ton = int()
total_cargo = float()
cargo_ton_bus = int()
cargo_ton_truck = int()
cargo_ton_train = int()
price_for_bus = float()
price_for_truck = float()
price_for_train = float()
for seuqence in range(cargos):
    cargo_weight = float(input())
    if cargo_weight < 4:
        vehicle_type = "bus"
        cargo_ton_bus += cargo_weight
        total_cargo += cargo_weight
        price_for_bus += (cargo_weight * 200)
    elif cargo_weight < 12:
        vehicle_type = "truck"
        cargo_ton_truck += cargo_weight
        total_cargo += cargo_weight
        price_for_truck += (cargo_weight * 175)
    else:
        vehicle_type = "train"
        cargo_ton_train += cargo_weight
        total_cargo += cargo_weight
        price_for_train += (cargo_weight * 120)
percentage_bus = cargo_ton_bus / total_cargo * 100
percentage_truck = cargo_ton_truck / total_cargo * 100
percentage_train = cargo_ton_train / total_cargo * 100
average_price = (200 * cargo_ton_bus + 175 * cargo_ton_truck + 120 * cargo_ton_train) / total_cargo
print(f"{average_price:.2f}")
print(f"{percentage_bus:.2f}%")
print(f"{percentage_truck:.2f}%")
print(f"{percentage_train:.2f}%")