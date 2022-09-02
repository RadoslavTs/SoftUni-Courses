period = int(input())
number_of_doctors = 7
examined_patients = int()
unexamined_patients = int()
total_patients = int()
for sequence in range(1, period + 1):
    patients_number = int(input())
    if sequence % 3 == 0:
        if unexamined_patients > examined_patients:
            number_of_doctors += 1
    if patients_number <= number_of_doctors:
        examined_patients += patients_number
        total_patients += examined_patients
    else:
        unexamined_patients += (patients_number - number_of_doctors)
        examined_patients += number_of_doctors
print(f"Treated patients: {examined_patients}.")
print(f"Untreated patients: {unexamined_patients}.")
