# Program to sort a list without using sort() method

numbers = [5, 2, 8, 1, 3]             # Create a list of numbers

n = len(numbers)                      # Find length of list

for i in range(n):                    # Outer loop for passes
    for j in range(0, n-i-1):         # Inner loop for comparison
        if numbers[j] > numbers[j+1]: # Check if current element is greater
            temp = numbers[j]         # Store value temporarily
            numbers[j] = numbers[j+1] # Swap elements
            numbers[j+1] = temp       # Complete the swap

print("Sorted list:", numbers)        # Display sorted list

# Output Example
# Sorted list: [1, 2, 3, 5, 8]
