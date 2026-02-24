# Problem 5
# Program to calculate Compound Interest

# Taking input from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

# Calculating Compound Interest
amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal

# Printing the result
print("The Compound Interest is:", compound_interest)

# output
# Enter the principal amount: 1000
#Enter the rate of interest: 5
#Enter the time (in years): 2
#The Compound Interest is: 102.5
