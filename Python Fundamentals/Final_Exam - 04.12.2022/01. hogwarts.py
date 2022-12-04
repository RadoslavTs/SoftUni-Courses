spell = input()
command = input()
while command != "Abracadabra":
    command_split = command.split()
    action = command_split[0]
    if action == "Abjuration":
        spell = spell.upper()
        print(spell)
    elif action == "Necromancy":
        spell = spell.lower()
        print(spell)
    elif action == "Illusion":
        index = int(command_split[1])
        letter = command_split[2]
        if 0 <= index < len(spell):
            spell = spell[:index] + letter + spell[index+1:]
            print("Done!")
        else:
            print("The spell was too weak.")
    elif action == "Divination":
        first_substring = command_split[1]
        second_substring = command_split[2]
        if first_substring in spell:
            spell = spell.replace(first_substring, second_substring)
            print(spell)
        else:
            pass
    elif action == "Alteration":
        substring = command_split[1]
        if substring in spell:
            spell = spell.replace(substring, "", 1)
            print(spell)
        else:
            pass
    else:
        print("The spell did not work!")
    command = input()
