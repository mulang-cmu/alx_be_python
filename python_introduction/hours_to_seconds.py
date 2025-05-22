"""
Objective: Demonstrate understanding of variable assignments and arithmetic operations by converting a given number of hours into seconds.
Task Description:
    Write Python script that converts a specific number of hours into seconds.
    This task reinforces the concept of arithmetic operations within a practical context.

Instructions:
    1. Create a file named hours_to_seconds.py.
    2. Define a variable named hours and assign it a value representing the number of hours you want to convert to seconds. Use hours = 2.
    3. Calculate the number of seconds in the given hours. Remember, there are 3600 seconds in an hour (since there are 60 minutes in an hour and 60 seconds in a minute, thus 60 x 60 = 3600).
    4. Store the result of the conversion in a variable named seconds.
"""

#defining variables
hours = 2
seconds = hours * 60 * 60


# Print the result in the format: [hours] hour(s) is [seconds] seconds.
if __name__ == "__main__":
    print(f"{hours} (s) is {seconds} seconds.")