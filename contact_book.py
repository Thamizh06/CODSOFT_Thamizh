# Run this is in an code editor like VS code
# The program can do the following tasks:Store, Add, Display, Search ,Modify, Delete Contacts
# Thank you <3
class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}")
            print(f"Phone Number: {contact.phone_number}")
            print(f"Email: {contact.email}")
            print(f"Address: {contact.address}")
            print("------------------------")

    def search_contact(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term.lower() in contact.phone_number.lower():
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, contact, updated_contact):
        for i, c in enumerate(self.contacts):
            if c == contact:
                self.contacts[i] = updated_contact
                break

    def delete_contact(self, contact):
        self.contacts.remove(contact)

if __name__ == "__main__":
    contact_manager = ContactManager()

    while True:
        print("Contact Management System")
        print("---------")
        print("1. Store Contact")
        print("2. Add Contact")
        print("3. Display Contacts")
        print("4. Search Contact")
        print("5. Modify Contact")
        print("6. Delete Contact")
        print("7. Exit")
        selection = input("Enter your selection: ")

        if selection == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone_number, email, address)
            contact_manager.add_contact(contact)
            print("Contact stored successfully.")
        elif selection == "2":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone_number, email, address)
            contact_manager.add_contact(contact)
            print("Contact added successfully.")
        elif selection == "3":
            contact_manager.view_contacts()
        elif selection == "4":
            search_term = input("Enter search term(search term can be either the name or phone no.): ")
            found_contacts = contact_manager.search_contact(search_term)
            if found_contacts:
                for contact in found_contacts:
                    print(f"Name: {contact.name}")
                    print(f"Phone Number: {contact.phone_number}")
                    print(f"Email: {contact.email}")
                    print(f"Address: {contact.address}")
                    print("------------------------")
            else:
                print("No contacts found.")
        elif selection == "5":
            name = input("Enter name of contact to modify: ")
            found_contacts = contact_manager.search_contact(name)
            if found_contacts:
                contact = found_contacts[0]
                updated_name = input("Enter updated name: ")
                updated_phone_number = input("Enter updated phone number: ")
                updated_email = input("Enter updated email: ")
                updated_address = input("Enter updated address: ")
                updated_contact = Contact(updated_name, updated_phone_number, updated_email, updated_address)
                contact_manager.update_contact(contact, updated_contact)
                print("Contact modified successfully.")
            else:
                print("Contact not found.")
        elif selection == "6":
            name = input("Enter name of contact to delete: ")
            found_contacts = contact_manager.search_contact(name)
            if found_contacts:
                contact = found_contacts[0]
                contact_manager.delete_contact(contact)
                print("Contact deleted successfully.")
            else:
                print("Contact not found.")
        elif selection == "7":
            print("Exiting contact management system...")
            break

