# deposit = str()
# account_balance = float()
# while True:
#     deposit = input()
#     if deposit == "NoMoreMoney":
#         break
#     if float(deposit) < 0:
#         print("Invalid operation!")
#         break
#     account_balance += float(deposit)
#     deposit = float(deposit)
#     print(f"Increase: {deposit:.2f}")
# print(f"Total: {account_balance:.2f}")

deposit = input()
balance = 0
while deposit != "NoMoreMoney":
    current_sum = float(deposit)
    if current_sum < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {current_sum:.2f}")
    balance += current_sum
    deposit = input()
print(f"Total: {balance:.2f}")
