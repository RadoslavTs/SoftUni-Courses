required_sum = float(input())
collected_sum = float()
transaction_sequence = 0
cash_payments_total = float()
card_payments_total = float()
total_transaction_cash = int()
total_transaction_card = int()
while collected_sum < required_sum:
    current_sum = input()
    transaction_sequence += 1
    if current_sum == "End":
        print("Failed to collect required money for charity.")
        break
    current_sum_float = float(current_sum)
    if transaction_sequence % 2 == 1:
        if current_sum_float > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            total_transaction_cash += 1
            collected_sum += current_sum_float
            cash_payments_total += current_sum_float
    if transaction_sequence % 2 == 0:
        if current_sum_float < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            total_transaction_card += 1
            collected_sum += current_sum_float
            card_payments_total += current_sum_float
if collected_sum >= required_sum:
    print(f"Average CS: {(cash_payments_total / total_transaction_cash):.2f}")
    print(f"Average CC: {(card_payments_total / total_transaction_card):.2f}")
