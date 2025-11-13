# === Simple Contact Book ===

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print("Contact added.")

def view_contacts(contacts):
    print("=== Contacts ===")
    if len(contacts) == 0:
        print("No contacts found.")
    else:
        for name in contacts:
            print(name, "-", contacts[name])

def contact_book_app():
    contacts = {}
    while True:
        print("\n1. Add Contact\n2. View Contacts\n3. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice.")

contact_book_app()
