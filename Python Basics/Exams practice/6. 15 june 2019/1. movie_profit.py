movie_name = input()
days_count = int(input())
ticket_count = int(input())
ticket_price = float(input())
cinema_share = int(input())
daily_income = ticket_count * ticket_price
total_income = daily_income * days_count
cinema_tax = total_income * cinema_share / 100
total_income -= cinema_tax
print(f"The profit from the movie {movie_name} is {total_income:.2f} lv.")