# user_interaction.py

def get_user_input(prompt):
    """Prompts the user for input and returns the response."""
    return input(prompt)

def display_contacts(contacts):
    """Displays a list of contacts to the user."""
    if not contacts:
        print("No contacts available.")
    else:
        print("Contacts:")
        for contact in contacts:
            print(f"- {contact}")

def display_message(message):
    """Displays a message to the user."""
    print(message)
