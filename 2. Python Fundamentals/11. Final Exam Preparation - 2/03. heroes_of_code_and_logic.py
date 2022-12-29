number_of_heroes = int(input())
hero_dictionary = {}
max_mana = 200
max_health = 100
for sequence in range(number_of_heroes):
    hero, health, mana = input().split()
    if hero not in hero_dictionary.keys():
        hero_dictionary[hero] = [int(health), int(mana)]
command = input()
while command != "End":
    command_split = command.split(" - ")
    action = command_split[0]
    if action == "CastSpell":
        hero = command_split[1]
        mana_needed = int(command_split[2])
        spell_name = command_split[3]
        if hero in hero_dictionary.keys():
            if hero_dictionary[hero][1] >= mana_needed:
                hero_dictionary[hero][1] -= mana_needed
                print(f"{hero} has successfully cast {spell_name} and now has {hero_dictionary[hero][1]} MP!")
            else:
                print(f"{hero} does not have enough MP to cast {spell_name}!")
    elif action == "TakeDamage":
        hero = command_split[1]
        damage = int(command_split[2])
        attacker = command_split[3]
        if hero in hero_dictionary.keys():
            if hero_dictionary[hero][0] > damage:
                hero_dictionary[hero][0] -= damage
                print(f"{hero} was hit for {damage} HP by {attacker} and now has {hero_dictionary[hero][0]} HP left!")
            else:
                print(f"{hero} has been killed by {attacker}!")
                del hero_dictionary[hero]
    elif action == "Recharge":
        hero = command_split[1]
        amount = int(command_split[2])
        if hero in hero_dictionary.keys():
            if amount + hero_dictionary[hero][1] > max_mana:
                recharge_amount = max_mana - hero_dictionary[hero][1]
                hero_dictionary[hero][1] = max_mana
                print(f"{hero} recharged for {recharge_amount} MP!")
            else:
                hero_dictionary[hero][1] += amount
                print(f"{hero} recharged for {amount} MP!")
    elif action == "Heal":
        hero = command_split[1]
        amount = int(command_split[2])
        if hero in hero_dictionary.keys():
            if amount + hero_dictionary[hero][0] > max_health:
                recharge_amount = max_health - hero_dictionary[hero][0]
                hero_dictionary[hero][0] = max_health
                print(f"{hero} healed for {recharge_amount} HP!")
            else:
                hero_dictionary[hero][0] += amount
                print(f"{hero} healed for {amount} HP!")
    command = input()

for hero in hero_dictionary:
    print(hero)
    print(f"  HP: {hero_dictionary[hero][0]}")
    print(f"  MP: {hero_dictionary[hero][1]}")
