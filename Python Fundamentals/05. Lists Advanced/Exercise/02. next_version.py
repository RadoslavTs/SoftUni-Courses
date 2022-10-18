initial_version = input()
final_version = ""
if int(initial_version[4]) < 9:
    final_version = initial_version[:4] + str(int(initial_version[4]) + 1)
elif int(initial_version[4]) == 9:
    if int(initial_version[2]) < 9:
        final_version = initial_version[:2] + str(int(initial_version[2]) + 1) + ".0"
    elif int(initial_version[2]) == 9:
        final_version = str(int(initial_version[0]) + 1) + ".0.0"
print(final_version)