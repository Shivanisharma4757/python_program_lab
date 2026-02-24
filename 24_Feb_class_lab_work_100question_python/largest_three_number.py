# Problem 3
# Program to find the largest of three numbers

# Taking input from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Checking which number is the largest
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

# Printing the largest number
print("The largest number is:", largest)

#output
#Enter first number: 12
#Enter second number: 5
#Enter third number: 45
#The largest number is: 45
