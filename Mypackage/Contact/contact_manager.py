# contact_manager.py

from .contact import Contact

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        """Adds a new contact to the contact list."""
        new_contact = Contact(name, phone)
        self.contacts.append(new_contact)

    def list_contacts(self):
        """Returns a list of all contacts."""
        return self.contacts

    def find_contact(self, name):
        """Finds a contact by name."""
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None
