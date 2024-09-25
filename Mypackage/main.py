# main.py

from Contact import ContactManager
from Contact import get_user_input, display_contacts, display_message

def run_contact_manager():
    """Runs the contact management system."""
    contact_manager = ContactManager()

    while True:
        action = get_user_input("Choose an action (add, list, find, quit): ").strip().lower()

        if action == "add":
            name = get_user_input("Enter the contact name: ")
            phone = get_user_input("Enter the contact phone number: ")
            contact_manager.add_contact(name, phone)
            display_message(f"Contact '{name}' added.")

        elif action == "list":
            contacts = contact_manager.list_contacts()
            display_contacts(contacts)

        elif action == "find":
            name = get_user_input("Enter the contact name to find: ")
            contact = contact_manager.find_contact(name)
            if contact:
                display_message(f"Found: {contact}")
            else:
                display_message("Contact not found.")

        elif action == "quit":
            display_message("Exiting the contact manager.")
            break

        else:
            display_message("Invalid action. Please try again.")

if __name__ == "__main__":
    run_contact_manager()
