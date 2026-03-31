import numpy as np

# Input: NumPy array
arr = np.array([10, 20, 30, 40, 50])

# Normalize between 0 and 1
normalized = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))

# Output
print("Normalized array:", normalized)

#output
#Normalized array: [0.   0.25 0.5  0.75 1.  ]
