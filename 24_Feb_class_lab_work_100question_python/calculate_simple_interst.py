# Problem 4
# Program to calculate Simple Interest

# Taking input from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

# Calculating Simple Interest
simple_interest = (principal * rate * time) / 100

# Printing the result
print("The Simple Interest is:", simple_interest)

#output
#Enter the principal amount: 1000
#Enter the rate of interest: 5
#Enter the time (in years): 2
#The Simple Interest is: 100.0
