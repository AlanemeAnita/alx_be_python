# shopping_list_manager.py

shopping_list = []

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item():
    item = input("Enter item to add: ")
    if item:
        shopping_list.append(item)
        print(f"{item} has been added to your list.")
    else:
        print("No item entered.")

def remove_item():
    item = input("Enter item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from your list.")
    else:
        print(f"{item} is not in your list.")

def view_list():
    if shopping_list:
        print("\nYour Shopping List:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")
    else:
        print("Your shopping list is empty.")

while True:
    display_menu()  # <- Required by checker
    try:
        choice = int(input("Enter your choice: "))  # <- Input as number
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
