company_name = str(input())
ticket_count = int(input())
child_tickets = int(input())
adult_ticket_price = float(input())
service_tax = float(input())
child_ticket_price = adult_ticket_price * 0.3 + service_tax
adult_ticket_price = adult_ticket_price + service_tax
adult_tickets_profit = ticket_count * adult_ticket_price
child_tickets_profit = child_ticket_price * child_tickets
earnings = adult_tickets_profit + child_tickets_profit
profit = earnings * 0.2
result = "{:.2f}".format(profit)
print(f"The profit of your agency from {company_name} tickets is {result} lv.")