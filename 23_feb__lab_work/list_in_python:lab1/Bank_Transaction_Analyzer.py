# Program Name: Bank Transaction Analyzer

transactions = [20000, -5000, 15000, -12000, 8000, -3000]

# Calculate total balance
balance = sum(transactions)

# Find largest withdrawal
withdrawals = [t for t in transactions if t < 0]
largest_withdrawal = min(withdrawals)

# Count deposits greater than 10000
large_deposits = len([t for t in transactions if t > 10000])

print("Total Balance:", balance)
print("Largest Withdrawal:", largest_withdrawal)
print("Deposits > 10000:", large_deposits)

# Output:
# Total Balance: 23000
# Largest Withdrawal: -12000
# Deposits > 10000: 2
