# Program to sort dictionary by values

data = {"a": 5, "b": 2, "c": 8, "d": 1}   # Create dictionary

sorted_items = sorted(data.items(), key=lambda x: x[1])  # Sort dictionary items by value

sorted_dict = dict(sorted_items)         # Convert sorted items back to dictionary

print("Dictionary sorted by values:", sorted_dict)  # Display sorted dictionary

# Output Example
# Dictionary sorted by values: {'d': 1, 'b': 2, 'a': 5, 'c': 8}
