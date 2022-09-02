location_number = int(input())
total_gold_mined = 0
average_mined_gold = 0
days_mining = 0
for sequence in range(location_number):
    average_daily_gold_mining_required = float(input())
    days_mining = int(input())
    for sequence_two in range(days_mining):
        mined_gold = float(input())
        total_gold_mined += mined_gold
    average_mined_gold = total_gold_mined / days_mining
    difference = abs(average_daily_gold_mining_required - average_mined_gold)
    if average_mined_gold >= average_daily_gold_mining_required:
        print(f"Good job! Average gold per day: {average_mined_gold:.2f}.")
    else:
        print(f"You need {difference:.2f} gold.")
    total_gold_mined = 0
    average_mined_gold = 0
