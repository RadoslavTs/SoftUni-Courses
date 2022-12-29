tournament_days = int(input())
raised_money = int()
raised_money_total = int()
wins_count = int()
lose_count = int()
total_wins_count = int()
total_lose_count = int()
sport = float()
result = float()
for sequence in range(tournament_days):
    while sport != "Finish":
        sport = input()
        if sport == "Finish":
            if wins_count > lose_count:
                raised_money += raised_money * 0.1
                raised_money_total += raised_money
                raised_money = 0
                total_wins_count += wins_count
                total_lose_count += lose_count
                wins_count = 0
                lose_count = 0
                sport = ""
                break
            else:
                raised_money_total += raised_money
                raised_money = 0
                total_wins_count += wins_count
                total_lose_count += lose_count
                wins_count = 0
                lose_count = 0
                sport = ""
                break
        else:
            result = input()
        if result == "win":
            raised_money += 20
            wins_count += 1
        else:
            lose_count += 1
if total_wins_count > total_lose_count:
    raised_money_total += raised_money_total * 0.2
    print(f"You won the tournament! Total raised money: {raised_money_total:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {raised_money_total:.2f}")
