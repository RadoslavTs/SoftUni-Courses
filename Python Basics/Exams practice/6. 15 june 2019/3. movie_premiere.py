movie_name = input()
package_type = input()
ticket_count = int(input())
ticket_price = 0
if movie_name == "John Wick":
    if package_type == "Drink":
        ticket_price = 12
    elif package_type == "Popcorn":
        ticket_price = 15
    else:
        ticket_price = 19
elif movie_name == "Star Wars":
    if package_type == "Drink":
        ticket_price = 18
    elif package_type == "Popcorn":
        ticket_price = 25
    else:
        ticket_price = 30
else:
    if package_type == "Drink":
        ticket_price = 9
    elif package_type == "Popcorn":
        ticket_price = 11
    else:
        ticket_price = 14
total_price = ticket_price * ticket_count
if movie_name == "Star Wars" and ticket_count >= 4:
    total_price *= 0.7
if movie_name == "Jumanji" and ticket_count == 2:
    total_price *= 0.85
print(f"Your bill is {total_price:.2f} leva.")
