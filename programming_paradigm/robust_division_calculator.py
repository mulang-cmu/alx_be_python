"""
1. Robust Division Calculator with Command Line Arguments (mandatory)
Objective: Implement a division calculator that robustly handles errors like division by zero and non-numeric inputs using command line arguments.
Task Description:
    Create two Python scripts: robust_division_calculator.py, which contains the division logic including error handling, and main.py, which interfaces with the user through the command line.
    robust_division_calculator.py:
        Define a function safe_divide(numerator, denominator) that performs division, handling potential errors:
        Division by Zero: Use a try-except block to catch ZeroDivisionError.
        Non-numeric Input: Attempt to convert arguments to floats. Use a try-except block to catch ValueError for non-numeric inputs.
        Return appropriate messages for errors or the result for successful division.
main.py for Command Line Interaction:
This script will import safe_divide from robust_division_calculator.py and use it to divide numbers provided as command line arguments.
"""
class NoneNumericInputError(Exception):
    def __init__(self):
        super().__init__("Error: Please enter numeric values only.")
    
class DivisionByZeroError(Exception):
    def __init__(self):
        super().__init__("Error: Cannot divide by zero.")

def safe_divide(numerator, denominator):
    try:
        nume = float(numerator)
        denom = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only." # NoneNumericInputError()
    
    if denom == 0:
        return "Error: Cannot divide by zero."

    else:
        return  nume / denom


