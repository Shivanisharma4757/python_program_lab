# Program to calculate Simple Interest

# Take principal amount as input
principal = float(input("Enter the principal amount: "))

# Take rate of interest as input (in percentage)
rate = float(input("Enter the rate of interest (per year): "))

# Take time period as input (in years)
time = float(input("Enter the time period (in years): "))

# Calculate simple interest using the formula: SI = (P * R * T) / 100
simple_interest = (principal * rate * time) / 100

# Display the result
print("The Simple Interest is:", simple_interest)