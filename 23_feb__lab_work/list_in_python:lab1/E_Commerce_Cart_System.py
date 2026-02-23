# Program Name: E-Commerce Cart System

cart = [2000, 1500, 2000, 800, 1200]

# Remove duplicates
cart = list(set(cart))

total = sum(cart)

# Apply discount
if total > 5000:
    total *= 0.90  # 10% discount

# Add GST 18%
total *= 1.18

print("Final Payable Amount:", round(total, 2))

# Output:
# Final Payable Amount: 5664.0
