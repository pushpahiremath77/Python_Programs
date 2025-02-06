contact_book = {}

def add_contact(name,phone):
    if name not in contact_book:
        contact_book[name] = phone
        print(f"Contact added successfully")
    else:
        print(f"{name} already present in contact book")

def delete_contact(name):
    if name in contact_book:
        del contact_book[name]
        print(f"{name} is deleted successfully from contact book")
    else:
        print(f"{name} not present in contact book")

def update_contact(name,new_phone):
    if name in contact_book:
        contact_book[name] = new_phone
        print(f"Updated the contact {name}")
    else:
        print(f"{name} not found in contact book")

def search_contact(name):
    if name not in contact_book:
        print(f"{name} is not in contact book")
    else:
        print(f"contact of {name}:")
        print(f"{name}:{contact_book[name]}")

def display_contact():
    if contact_book:
        print("Contacts:")
        for name,phone in contact_book.items():    
            print(f"{name}: {phone}")
    else:
        print("Contact book is empty")

def contact_menu():
    while True:
        print("1. Add a new contact")
        print("2. Delete a contact")
        print("3. Update a contact")
        print("4. search a contact")
        print("5. Display contacts")
        print("6. Exit")

        choice = int(input("Enter your choice:"))

        if choice==1:
            name = input("Enter name :")
            phone = input("Enter phone number:")
            add_contact(name,phone)

        elif choice==2:
            name = input("Enter the name to delete:")
            delete_contact(name)
        
        elif choice==3:
            name = input("Enter the name to update the phone number:")
            new_phone = input("Enter the new phone number:")
            update_contact(name,new_phone)
        
        elif choice==4:
            name = input("Enter name to search:")
            search_contact(name)

        elif choice==5:
            display_contact()

        elif choice==6:
            break
        else:
            print("Invalid choice")

contact_menu()


