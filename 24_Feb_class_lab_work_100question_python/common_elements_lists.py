# Program to find common elements between two lists

list1 = [1, 2, 3, 4]                   # Create first list
list2 = [3, 4, 5, 6]                   # Create second list

common = []                            # Create empty list for common elements

for num in list1:                      # Loop through first list
    if num in list2:                   # Check if element exists in second list
        common.append(num)             # Add element to common list

print("Common elements:", common)      # Display common elements

# Output Example
# Common elements: [3, 4]
