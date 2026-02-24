# Program to reverse a list without using reverse() method

numbers = [1, 2, 3, 4, 5]              # Create a list of numbers

reversed_list = []                     # Create empty list for reversed result

for num in numbers:                    # Loop through each element
    reversed_list = [num] + reversed_list  # Add element at beginning of new list

print("Reversed list:", reversed_list) # Display reversed list

# Output Example
# Reversed list: [5, 4, 3, 2, 1]
