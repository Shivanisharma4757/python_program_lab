# Function to swap keys and values
def swap_dict(d):
    swapped = {}

    for key, value in d.items():
        swapped[value] = key

    return swapped


# Input
data = {
    "A": 1,
    "B": 2,
    "C": 3
}

# Output
result = swap_dict(data)

print("Swapped dictionary:", result)

#output
#Swapped dictionary: {1: 'A', 2: 'B', 3: 'C'}
