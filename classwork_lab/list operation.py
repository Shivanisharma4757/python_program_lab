# Python Program: Sum of a User-Entered List

# Step 1: Ask the user how many numbers they want to enter
n = int(input("How many numbers do you want in the list? "))

# Step 2: Initialize an empty list
numbers = []

# Step 3: Take input from the user
for i in range(n):
    num = float(input(f"Enter number {i+1}: "))  # Use float for decimal numbers
    numbers.append(num)  # Add number to the list

# Step 4: Calculate sum using sum() function
total = sum(numbers)

# Step 5: Display the sum
print("The list you entered:", numbers)
print("Sum of the list:", total)

output

How many numbers do you want in the list? 5
Enter number 1: 2
Enter number 2: 4
Enter number 3: 6
Enter number 4: 8
Enter number 5: 10
The list you entered: [2.0, 4.0, 6.0, 8.0, 10.0]
Sum of the list: 30.0
