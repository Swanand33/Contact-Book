from contact_book.contact_manager import ContactManager
from contact_book.file_handler import FileHandler

def main():
    file_handler = FileHandler('data/contacts.json')
    contact_manager = ContactManager(file_handler)

    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            contact_manager.add_contact(name, phone, email)
        elif choice == '2':
            contact_manager.view_contacts()
        elif choice == '3':
            name = input("Enter name to search: ")
            contact_manager.search_contact(name)
        elif choice == '4':
            name = input("Enter name to delete: ")
            contact_manager.delete_contact(name)
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()