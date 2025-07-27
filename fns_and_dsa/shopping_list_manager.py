shopping_list = []

def display_menu():
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

display_menu()

try:
    choice = int(input("Enter your choice: "))
except ValueError:
    print("Invalid input")
