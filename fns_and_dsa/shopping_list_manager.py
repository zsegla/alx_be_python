shopping_list  = []

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Display Items")
    print("4. Exit")

def add_item():
    item = input(f"Enter the item to add: ")
    shopping_list.append(item)

def remove_item():
    item = input(f"Enter item to remove from shopping list: ")
    if item in shopping_list:
        shopping_list.remove(item)
    else:
        raise ValueError(f"Item '{item}' not found in the shopping list.")
    
def display_items():
    if not shopping_list:
        print("Shopping list is empty.")
    else:
        print("Shopping List:")
        for item in shopping_list:
            print(f"- {item}")

def main():
    display_menu()
    user_choice = input(": ").strip().lower()
    while user_choice != 'exit':
        if user_choice == 'add':
            add_item()
        elif user_choice == 'remove':
            remove_item()
        elif user_choice == 'display':
            display_items()
        else:
            print("Invalid choice. Please choose 'add', 'remove', 'display', or 'exit'.")
        display_menu()
        user_choice = input("Choose an action: add, remove, display, or exit: ").strip().lower()

if __name__ == "__main__":
    main()  