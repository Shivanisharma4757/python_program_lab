# Program to count frequency of elements in a list

numbers = [1, 2, 2, 3, 3, 3, 4]        # Create a list with repeated elements

freq = {}                              # Create an empty dictionary to store frequency

for num in numbers:                    # Loop through each element in the list
    if num in freq:                    # Check if element already exists in dictionary
        freq[num] = freq[num] + 1      # Increase frequency count
    else:                              # If element does not exist
        freq[num] = 1                  # Initialize frequency with 1

print("Frequency of elements:", freq)  # Display frequency dictionary

# Output Example
# Frequency of elements: {1: 1, 2: 2, 3: 3, 4: 1}
