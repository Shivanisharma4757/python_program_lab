# Program to find the maximum value in a tuple

numbers = (10, 45, 23, 89, 12)        # Create a tuple of numbers

maximum = numbers[0]                  # Assume first element is the maximum

for num in numbers:                   # Loop through each element in tuple
    if num > maximum:                 # Check if current element is greater
        maximum = num                 # Update maximum value

print("Maximum value:", maximum)      # Display maximum value

# Output Example
# Maximum value: 89
