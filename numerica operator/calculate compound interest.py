# Program to calculate Compound Interest

# Take principal amount as input
principal = float(input("Enter the principal amount (P): "))

# Take annual interest rate as input (in percentage)
rate = float(input("Enter the annual interest rate (R%) : "))

# Take time period as input (in years)
time = float(input("Enter the time period in years (T): "))

# Take number of compounding periods per year
n = float(input("Enter number of times interest is compounded per year (n): "))

# Convert rate from percentage to decimal
rate_decimal = rate / 100

# Calculate compound interest using formula:
# A = P * (1 + R/n)^(n*T)
amount = principal * (1 + rate_decimal/n)**(n*time)

# Calculate the interest earned
compound_interest = amount - principal

# Display the results
print("Compound Interest: {:.2f}".format(compound_interest))

print("Total Amount after", time, "years: {:.2f}".format(amount))

# output
# Enter the principal amount (P): 1000
# Enter the annual interest rate (R%) : 5
# Enter the time period in years (T): 2
# Enter number of times interest is compounded per year (n): 1

# Compound Interest: 102.50
# Total Amount after 2.0 years: 1102.50
