# main.py
from shopping_list_manager import display_menu, add_item, remove_item, view_list

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            item = input("Enter the item to add: ")
            if item:
                add_item(item)
            else:
                print("Item cannot be empty!")

        elif choice == '2':
            item = input("Enter the item to remove: ")
            if item:
                remove_item(item)
            else:
                print("Item cannot be empty!")

        elif choice == '3':
            view_list()

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()