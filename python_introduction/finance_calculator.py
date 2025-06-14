"""
Objective: Use user input, variables, and arithmetic operations to calculate and provide feedback on a user’s monthly savings and potential future savings without applying conditional statements.
Task Description:
    You will create a script named finance_calculator.py. This script will calculate the user’s monthly savings based on inputted monthly income and expenses. It will then project these savings over a year, assuming a fixed interest rate, to demonstrate compound interest’s effect on savings.
Instructions:
    1. User Input for Financial Details:
        a. Prompt the user for their monthly income: “Enter your monthly income: ”.
        b. Ask for their total monthly expenses: “Enter your total monthly expenses: ”.
    2. Calculate Monthly Savings:
        Calculate the monthly savings by subtracting monthly expenses from the monthly income.
    3. Project Annual Savings:
        Assume a simple annual interest rate of 5%.
        Calculate the projected savings after one year, incorporating the interest. 
        Use the simplified formula for annual savings projection: (Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)).
    4. Output Results:
        Display the user’s monthly savings.
        Display the projected annual savings after including interest.
"""
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses  # <- Match this exactly

projected_savings = (monthly_savings * 12) + int((monthly_savings * 12 * 0.05))

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")

"""
# Declaring Variables
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - mopython versionnthly_expenses

# Project Annual Savings:
projected_savings = (monthly_savings * 12) + int((monthly_savings * 12 * 0.05))

# Display the user’s monthly savings.
# Display the projected annual savings after including interest.
if __name__ == "__main__":
    print(f"Your monthly savings are ${monthly_savings}.")
    print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
"""
