import json
import os

class FileHandler:
    def __init__(self, filepath):
        self.filepath = filepath
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w') as file:
                json.dump([], file)

    def load_contacts(self):
        with open(self.filepath, 'r') as file:
            return json.load(file)

    def save_contacts(self, contacts):
        with open(self.filepath, 'w') as file:
            json.dump(contacts, file)
