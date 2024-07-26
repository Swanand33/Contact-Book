from .file_handler import FileHandler

class ContactManager:
    def __init__(self, file_handler):
        self.file_handler = file_handler
        self.contacts = self.file_handler.load_contacts()

    def add_contact(self, name, phone, email):
        new_contact = {
            'name': name,
            'phone': phone,
            'email': email
        }
        self.contacts.append(new_contact)
        self.file_handler.save_contacts(self.contacts)

    def get_all_contacts(self):
        return self.contacts

    def search_contact(self, search_term):
        return [contact for contact in self.contacts if search_term.lower() in contact['name'].lower()]

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact['name'].lower() != name.lower()]
        self.file_handler.save_contacts(self.contacts)
