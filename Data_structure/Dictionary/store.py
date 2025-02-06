store = {}

def add_item(item,price):
    if item in store:
        print(f"{item} already present in store")
    else:
        store[item] = price
        print(f"Item {item} added successfully")

def view_price(item):
    if item not in store:
        print(f"{item} not found in store")
    else:
        print(f"Price of {item} is {store[item]}")

def display_items():
    if store:
        print("List of items & price")
        for item,price in store.items():
            print(f"{item}:{price}")
    else:
        print("There are no items in store")

def store_menu():
    print("Welcome to MY SHOP")

    while True:
        print("1. Add a new item")
        print("2. View a item price")
        print("3. Display items")
        print("4. Exit")

        choice = int(input("Enter your choice:"))

        if choice==1:
            item = input("Enter name of item:")
            price = input("Enter price:")
            add_item(item,price)
        
        elif choice==2:
            item = input("Enter item to view price:")
            view_price(item)

        elif choice==3:
            display_items()

        elif choice==4:
            break
        
        else:
            print("Invalid choice")

store_menu()