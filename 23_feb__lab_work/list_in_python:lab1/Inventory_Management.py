# Program Name: Inventory Management

stock = [25, 0, 5, 12, 0, 8, 50]

# Remove items with 0 stock
stock = [s for s in stock if s != 0]

# Add restock (add 50 units) to items below 10
for i in range(len(stock)):
    if stock[i] < 10:
        stock[i] += 50

# Find total inventory count
total_inventory = sum(stock)

print("Updated Stock:", stock)
print("Total Inventory Count:", total_inventory)

# Output:
# Updated Stock: [25, 55, 12, 58, 50]
# Total Inventory Count: 200
