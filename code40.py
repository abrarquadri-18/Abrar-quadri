balance = float(input("Enter balance: "))
amount = float(input("Enter withdrawal amount: "))
minimum = float(input("Enter minimum balance: "))

if amount <= 0:
    print("Invalid amount")
elif amount > balance:
    print("Insufficient balance")
elif balance - amount < minimum:
    print("Withdrawal rejected: Minimum balance required")
else:
    balance = balance - amount
    print("Withdrawal approved")
    print("Remaining balance =", balance)
    