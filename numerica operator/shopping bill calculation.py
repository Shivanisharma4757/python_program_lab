# Number of notebooks and their cost
notebooks = 3
cost_per_notebook = 45

# Number of pens and their cost
pens = 2
cost_per_pen = 20

# Calculate total cost of notebooks
total_notebooks_cost = notebooks * cost_per_notebook

# Calculate total cost of pens
total_pens_cost = pens * cost_per_pen

# Calculate total bill amount by adding notebook and pen costs
total_bill = total_notebooks_cost + total_pens_cost

# Amount given by customer
amount_given = 500

# Calculate remaining balance after payment
remaining_balance = amount_given - total_bill

# Display the results
print("Total bill amount: ₹", total_bill)
print("Remaining balance: ₹", remaining_balance)