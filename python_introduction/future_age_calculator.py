"""
Objective: Practice receiving user input in Python and perform a simple arithmetic operation to calculate the user’s age in a future year.
Task Description:
    Create a Python script that asks the user for their current age and then calculates how old they will be in a specific future year. 
    This task introduces handling user input and reinforces arithmetic operations.

Instructions:
    1. Create a file named future_age_calculator.py.
    2. Prompt the user to input their current age with the question: “How old are you? ”.
    3. Assume the user will input a valid integer value.
    4. Calculate how old the user will be in the year 2050. To keep calculations simple, assume the current year is 2023. Therefore, you need to add 27 years to the user’s current age.
    5. Print the user’s age in 2050 in the format: In 2050, you will be [age] years old.
    6. Expected Script Flow:
        The script prompts the user for their current age.
        The user enters their age.
        The script calculates and prints how old the user will be in 2050.
        Example Interaction:
"""

#defining variables
current_age = int(input("How old are you? "))
current_year = 2023
final_year = 2050
age_difference = final_year - current_year

# printing the output
# If the user inputs 30 when prompted for their current age, the output should be:
if __name__ == "__main__":
    print(f"In {final_year}, you will be {current_age + age_difference} years old.")
