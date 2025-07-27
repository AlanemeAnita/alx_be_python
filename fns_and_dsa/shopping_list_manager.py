# shopping_list_manager.py

# Define the shopping list as a global list
shopping_list = []

# Define the display_menu function
def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# Define the add_item function
def add_item():
    item = input("Enter item to add: ")
    if item:
        shopping_list.append(item)
        print(f"{item} has been added to your list.")
    else:
        print("No item entered.")

# Define the remove_item function
def remove_item():
    item = input("Enter item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from your list.")
    else:
        print(f"{item} is not in your list.")

# Define the view_list function
def view_list():
    if shopping_list:
        print("\nYour Shopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
    else:
        print("Your shopping list is empty.")

# Main loop
while True:
    display_menu()  # <- This makes sure the function is defined and called
    try:
        choice = int(input("Enter your choice: "))  # <- Input as a number
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        add_item()
    elif choice == 2:
        remove_item()
    elif choice == 3:
        view_list()
    elif choice == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
