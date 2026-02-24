# Program to find factorial using while loop

num = int(input("Enter a number: "))  # User se number input
fact = 1                              # Factorial store karne ke liye variable
i = 1                                 # Loop counter

while i <= num:                       # Jab tak i num se chota ya equal hai
    fact = fact * i                   # factorial multiply karte jao
    i += 1                            # counter increase karo

print("Factorial:", fact)             # Final factorial print

# Output Example
# Enter a number: 5
# Factorial: 120
