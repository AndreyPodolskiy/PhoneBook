
class PhoneBook:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_contacts(self):
        try:
            with open(self.file_name, 'r') as file:
                contacts = file.readlines()
            return [contact.strip() for contact in contacts]
        except FileNotFoundError:
            return []

    def save_contacts(self, contacts):
        with open(self.file_name, 'w') as file:
            for contact in contacts:
                file.write(contact + '\n')
