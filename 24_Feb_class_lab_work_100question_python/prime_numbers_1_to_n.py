# Program to print all prime numbers between 1 and N

n = int(input("Enter value of N: "))   # Take value of N from user
num = 2                                # Start checking from number 2

while num <= n:                        # Loop runs from 2 to N
    i = 2                              # Initialize divisor variable
    is_prime = True                    # Assume number is prime

    while i <= num // 2:               # Check divisibility up to half of the number
        if num % i == 0:               # If number is divisible
            is_prime = False           # Mark number as not prime
            break                      # Exit inner loop
        i = i + 1                      # Increase divisor

    if is_prime:                       # If number is still prime
        print(num)                     # Print the prime number

    num = num + 1                      # Move to next number

# Output Example
# Enter value of N: 10
# 2
# 3
# 5
# 7
