# Program to find sum of values in dictionary

data = {"a": 10, "b": 20, "c": 30}      # Create dictionary

total = 0                               # Variable to store sum

for value in data.values():             # Loop through dictionary values
    total += value                      # Add values to total

print("Sum of dictionary values:", total)  # Display sum

# Output Example
# Sum of dictionary values: 60
