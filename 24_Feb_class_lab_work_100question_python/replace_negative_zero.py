# Program to replace negative numbers in a list with zero

numbers = [5, -3, 8, -1, 7]              # Create list containing negative numbers

for i in range(len(numbers)):            # Loop through index of list
    if numbers[i] < 0:                   # Check if number is negative
        numbers[i] = 0                   # Replace negative value with zero

print("Updated list:", numbers)          # Display updated list

# Output Example
# Updated list: [5, 0, 8, 0, 7]
