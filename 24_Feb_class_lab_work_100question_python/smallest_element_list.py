# Program to find the smallest element in a list

numbers = [10, 45, 23, 89, 12]        # Create a list of numbers

smallest = numbers[0]                 # Assume first element is the smallest

for num in numbers:                   # Loop through each element in the list
    if num < smallest:                # Check if current element is smaller
        smallest = num                # Update smallest value

print("Smallest element:", smallest)  # Display the smallest element

# Output Example
# Smallest element: 10
