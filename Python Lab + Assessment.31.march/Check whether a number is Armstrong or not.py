def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    
    total = 0
    for digit in num_str:
        total += int(digit) ** power
    
    return total == n


# Example
print(is_armstrong(153))  # true
print(is_armstrong(123))  # false

# output
# true
# False
