# Program to return unique elements from a list using a function

def unique_list(lst):                     # Define function to get unique elements
    unique = []                           # Create empty list for unique values
    
    for item in lst:                      # Loop through each element
        if item not in unique:            # Check if element is not already in unique list
            unique.append(item)           # Add element to unique list
    
    return unique                         # Return unique list


numbers = [1, 2, 2, 3, 4, 4, 5]           # Define sample list

result = unique_list(numbers)             # Call function

print("Unique elements:", result)         # Display unique elements

# Output Example
# Unique elements: [1, 2, 3, 4, 5]
