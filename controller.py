
class PhoneBookController:
    def __init__(self, phone_book):
        self.phone_book = phone_book

    def show_all_contacts(self):
        contacts = self.phone_book.read_contacts()
        if contacts:
            return contacts
        else:
            return "Телефонная книга пуста."

    def add_contact(self, contact):
        contacts = self.phone_book.read_contacts()
        contacts.append(contact)
        self.phone_book.save_contacts(contacts)

    def find_contact(self, name):
        contacts = self.phone_book.read_contacts()
        for contact in contacts:
            if name in contact:
                return contact
        return "Контакт не найден."

    def update_contact(self, old_contact, new_contact):
        contacts = self.phone_book.read_contacts()
        if old_contact in contacts:
            index = contacts.index(old_contact)
            contacts[index] = new_contact
            self.phone_book.save_contacts(contacts)
            return "Контакт успешно обновлен."
        else:
            return "Контакт не найден."

    def delete_contact(self, contact):
        contacts = self.phone_book.read_contacts()
        if contact in contacts:
            contacts.remove(contact)
            self.phone_book.save_contacts(contacts)
            return "Контакт успешно удален."
        else:
            return "Контакт не найден."
