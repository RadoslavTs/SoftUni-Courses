guest_number = int(input())
reservation_codes = set()
arrived_guests = set()


for sequence in range(guest_number):
    guest_code = input()
    if len(guest_code) == 8:
        reservation_codes.add(guest_code)
non_arrived_guests = list(reservation_codes)
code_to_check = input()
while code_to_check != "END":
    arrived_guests.add(code_to_check)
    code_to_check = input()


non_arrived_guests = reservation_codes - arrived_guests
print(len(non_arrived_guests))

for guest in sorted(non_arrived_guests):
    print(guest)
