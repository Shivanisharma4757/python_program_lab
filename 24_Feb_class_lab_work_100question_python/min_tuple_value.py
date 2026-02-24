# Program to find the minimum value in a tuple

numbers = (10, 45, 23, 89, 12)        # Create a tuple of numbers

minimum = numbers[0]                  # Assume first element is the minimum

for num in numbers:                   # Loop through each element in tuple
    if num < minimum:                 # Check if current element is smaller
        minimum = num                 # Update minimum value

print("Minimum value:", minimum)      # Display minimum value

# Output Example
# Minimum value: 10
