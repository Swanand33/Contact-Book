# contact_book/contact.py

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f"Contact(name={self.name}, phone={self.phone}, email={self.email})"

    def to_dict(self):
        return {
            'name': self.name,
            'phone': self.phone,
            'email': self.email
        }

    @staticmethod
    def from_dict(data):
        return Contact(data['name'], data['phone'], data['email'])
