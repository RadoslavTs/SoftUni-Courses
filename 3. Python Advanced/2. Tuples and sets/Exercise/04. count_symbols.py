input_line = input()
input_line_sorted = sorted(list(input_line))
character_count_dict = {}
for ch in input_line_sorted:
    if ch not in character_count_dict.keys():
        character_count_dict[ch] = 1
    else:
        character_count_dict[ch] += 1
for character, occurance in character_count_dict.items():
    print(f'{character}: {occurance} time/s')
