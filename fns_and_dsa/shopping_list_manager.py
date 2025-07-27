<<<<<<< HEAD
shopping_list = []

def display_menu():
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

display_menu()

choice = int(input("Enter your choice: "))
=======
shopping_list = []  

def display_menu():  
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

while True:
    display_menu()  

    try:
        choice = int(input("Enter your choice: "))  
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"{item} added to the list.")
    elif choice == 2:
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed from the list.")
        else:
            print(f"{item} not found in the list.")
    elif choice == 3:
        print("Shopping List:")
        for item in shopping_list:
            print(f"- {item}")
    elif choice == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
