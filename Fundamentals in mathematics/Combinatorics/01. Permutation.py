from math import floor
print("Welcome to the combinatorics calculator!")
print("За да изберете тип на калкулацията въведете изберете номер от изброените:")
print("1. Пермутации (уникални стойности без повторения)")
print("2. Вариации (числа измежду други числа при строг ред)")
print("3. Комбинации (числа измежду други числа без значение подредбата)")
print("4. Вароятности")
print("5. Статистика")
calculation_type = int(input("Избор: "))

if calculation_type == 1:
    permutation_count = int(input("Веведете брой за пермутация: "))
    permutation_result = 1
    for sequence in range(1, permutation_count + 1):
        permutation_result *= sequence
    print(f"Резултатът от пермутацията е: {permutation_result}")

elif calculation_type == 2:
    variation_number_one = int(input("Въведете брой елементи за избор: "))
    variation_number_two = int(input("Въведете общ брой елементи: "))
    variation_result = 1
    for sequence_two in range(variation_number_two, variation_number_two-variation_number_one, -1):
        variation_result *= sequence_two
    print(f"Резултатът от вариацията е: {variation_result}")

elif calculation_type == 3:
    combination_number_one = int(input("Въведете брой елементи за избор: "))
    combination_number_two = int(input("Въведете общ брой елементи: "))
    combination_result = 1
    variation_result = 1
    permutation_result = 1
    for sequence_three in range(combination_number_two, combination_number_two-combination_number_one, -1):
        variation_result *= sequence_three
    for sequence_four in range(1, combination_number_one + 1):
        permutation_result *= sequence_four
    combination_result = variation_result / permutation_result
    print(f"Резултатът от комбинацията е: {combination_result:.0f}")

elif calculation_type == 4:
    probability_number_one = int(input("Въведете брой благоприятните случаи: "))
    probability_number_two = int(input("Въведете общ брой случаи: "))
    probability = probability_number_one / probability_number_two
    print(f"Вероятността е: {(probability*100):.6f}%")

elif calculation_type == 5:
    statistics_list = list(map(int, input("Въведете елементи разделени с разстояние: ").split()))
    statistics_set = set(statistics_list)
    modal_max = 0
    modal_value = ""
    total_sum = 0
    for digit in statistics_set:
        modal = statistics_list.count(digit)
        if modal > modal_max:
            modal_max = modal
            modal_value = digit
    for digit in statistics_list:
        total_sum += int(digit)
    average = total_sum / len(statistics_list)
    sorted_list = sorted(statistics_list)
    median = 0
    if len(sorted_list) % 2 != 0:
        median_index = floor(len(sorted_list)/2)
        median = sorted_list[median_index]
    else:
        first_index = int((len(sorted_list) / 2) - 1)
        second_index = int(len(sorted_list) / 2)
        median = (sorted_list[first_index] + sorted_list[second_index]) / 2
    print(f"Модата е: {modal_value}")
    print(f"Средната стойност е: {average:.2f}")
    print(f"Медианата е: {median}")
