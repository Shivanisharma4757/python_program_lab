# Program to Calculate Gross Salary
# Gross Salary = Basic Salary + HRA + DA

# Taking input from user
basic_input = input("Enter Basic Salary: ")
hra_input = input("Enter HRA amount: ")
da_input = input("Enter DA amount: ")

# Validation: Check if all inputs are numeric
if (basic_input.replace('.', '', 1).isdigit() and
    hra_input.replace('.', '', 1).isdigit() and
    da_input.replace('.', '', 1).isdigit()):
    
    basic = float(basic_input)
    hra = float(hra_input)
    da = float(da_input)

    # Basic salary should be greater than 0
    if basic > 0:
        
        # Calculating Gross Salary
        gross_salary = basic + hra + da
        
        print("\n----- Salary Details -----")
        print("Basic Salary: ₹", basic)
        print("HRA: ₹", hra)
        print("DA: ₹", da)
        print("Gross Salary: ₹", gross_salary)
    
    else:
        print("Error: Basic Salary must be greater than 0.")

else:
    print("Error: Please enter valid numeric values.")
