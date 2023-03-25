import re

def add_item(inventory):
    item_name = input("Enter the item name (alphanumeric): ")
    if not re.match("^[A-Za-z0-9]+$", item_name):
        print("Invalid input. Only alphanumeric characters are allowed.")
        return

    quantity = input("Enter the quantity (positive integer): ")
    if not quantity.isdigit() or int(quantity) <= 0:
        print("Invalid input. Please enter a positive integer.")
        return

    inventory[item_name] = inventory.get(item_name, 0) + int(quantity)
    print(f"{quantity} {item_name} added to the inventory.")

def update_item(inventory):
    item_name = input("Enter the item name (alphanumeric): ")
    if not re.match("^[A-Za-z0-9]+$", item_name):
        print("Invalid input. Only alphanumeric characters are allowed.")
        return
      
    if item_name not in inventory:
        print(f"{item_name} not found in the inventory.")
        return

    quantity = input("Enter the quantity to add (positive integer): ")
    if not quantity.isdigit() or int(quantity) <= 0:
        print("Invalid input. Please enter a positive integer.")
        return

    inventory[item_name] += int(quantity)
    print(f"{quantity} added to {item_name}. New quantity: {inventory[item_name]}")

def delete_item(inventory):
    item_name = input("Enter the item name to delete (alphanumeric): ")
    if not re.match("^[A-Za-z0-9]+$", item_name):
        print("Invalid input. Only alphanumeric characters are allowed.")
        return

    if item_name in inventory:
        del inventory[item_name]
        print(f"{item_name} deleted from the inventory.")
    else:
        print(f"{item_name} not found in the inventory.")

def view_inventory(inventory):
    if len(inventory) > 0:
        print("\nInventory:")
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")
    else:
        print("The inventory is empty.")

def main():
    inventory = {}
    while True:
        print("\nMenu:")
        print("1: Add Item")
        print("2: Update Item")
        print("3: Delete Item")
        print("4: View Inventory")
        print("5: Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            add_item(inventory)
        elif choice == 2:
            update_item(inventory)
        elif choice == 3:
            delete_item(inventory)
        elif choice == 4:
            view_inventory(inventory)
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
            

if __name__ == "__main__":
    main()