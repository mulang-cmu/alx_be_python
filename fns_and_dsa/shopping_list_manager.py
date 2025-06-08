"""
1. Shopping List Manager
mandatory
Objective: Utilize Python lists to create a simple shopping list manager that allows users to add items, view the current list, and remove items.

Task Description:
Create a Python script named shopping_list_manager.py that implements a simple interface for managing a shopping list. This task focuses on using lists to store and manipulate data dynamically.

Requirements:
Core Functionality:

Your script should start with an empty list named shopping_list.
Implement functionality to add items to the list, remove items, and display the current list.
User Interface:

Use a loop to continuously display a menu with options to the user until they choose to exit. The menu should offer options to add an item, remove an item, view the list, and exit.
For adding items, prompt the user for the item name and append it to shopping_list.
For removing items, ask the user for the item name and remove it from shopping_list. If the item is not found, display a message indicating so.
To view the list, print each item in shopping_list to the console.
Ensure your script handles invalid menu choices gracefully.
"""

# shopping_list_manager.py

shopping_list = []

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(item):
    shopping_list.append(item)
    print(f"'{item}' added to the list!")

def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' removed from the list!")
    else:
        print(f"'{item}' not found in the list!")

def view_list():
    if not shopping_list:
        print("Your shopping list is empty!")
    else:
        print("\nYour Shopping List:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")