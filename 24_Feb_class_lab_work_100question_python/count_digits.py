# Program to count the number of digits in a number

num = int(input("Enter a number: "))   # Take number input from user
count = 0                              # Initialize digit counter

while num > 0:                         # Loop runs while number is greater than 0
    num = num // 10                    # Remove last digit of the number
    count = count + 1                  # Increase digit count

print("Total digits:", count)          # Display the total number of digits

# Output Example
# Enter a number: 5678
# Total digits: 4
