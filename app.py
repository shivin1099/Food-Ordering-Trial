menu = {
    "burger": 80.20,
    "pizza" : 35.30,
    "pasta" : 100.10,
    "sprite" : 40.20,
}

order = []
def display_menu():
    print("Menu")
    for item , price in menu.items():
        print(f"{item} Rs.{price:.2f}")

def take_order():
    display_menu()
    while True:
        choice = input("Enter the items to order (or 'done' to finish):").lower()
        if choice == 'done':
            break 
        elif choice in menu:
            order.append(choice)
        else:
            print("Invalid item.Please choose from the menu.")

def calculateTotal():
    total = sum(menu[item] for item in order)
    return total

def main():
    print("Welcome to food ordering app")
    while True:
        print("\nOptions:")
        print("1. Take an order")
        print("2. View order")
        print("3. Calculate total")
        print("4. Quit")
        choice = input("Enter your choice:")
        if choice == '1':
            take_order()
        elif choice=='2':
            print("Your current order:")
            for item in order:
                print(item)
        elif choice == '3':
            total = calculateTotal()
            print(f"Total cost of your order: Rs.{total:.2f}")
        elif choice == '4':
            print("Thank you for using the Food Ordering App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__=="__main__":
    main()

