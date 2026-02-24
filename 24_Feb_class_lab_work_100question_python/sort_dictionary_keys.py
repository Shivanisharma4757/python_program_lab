# Program to sort dictionary by keys

data = {"b": 2, "a": 1, "d": 4, "c": 3}   # Create dictionary

sorted_keys = sorted(data)                # Sort dictionary keys

sorted_dict = {}                          # Create new dictionary

for key in sorted_keys:                   # Loop through sorted keys
    sorted_dict[key] = data[key]          # Add key-value pairs in order

print("Dictionary sorted by keys:", sorted_dict)   # Display sorted dictionary

# Output Example
# Dictionary sorted by keys: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
