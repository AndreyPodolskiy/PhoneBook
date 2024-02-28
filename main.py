

# 1. Открыть справочник
# 2. Сохраниить справончик
# 3. Показть все контакты
# 4. Создать контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход



from model import PhoneBook
from controller import PhoneBookController
from text import TextMessages
from view import View

def main():
    phone_book = PhoneBook('phone_book.txt')
    controller = PhoneBookController(phone_book)

    while True:
        choice = input(TextMessages.menu())
        
        if choice == '1':
            pass  # Открыть справочник
        elif choice == '2':
            pass  # Сохранить справочник
        elif choice == '3':
            contacts = controller.show_all_contacts()
            View.display_contacts(contacts)
        elif choice == '4':
            contact = input(TextMessages.input_contact())
            controller.add_contact(contact)
        elif choice == '5':
            name = input(TextMessages.input_name())
            contact = controller.find_contact(name)
            View.display_message(contact)
        elif choice == '6':
            old_contact = input(TextMessages.input_old_contact())
            new_contact = input(TextMessages.input_new_contact())
            message = controller.update_contact(old_contact, new_contact)
            View.display_message(message)
        elif choice == '7':
            contact = input(TextMessages.input_contact())
            message = controller.delete_contact(contact)
            View.display_message(message)
        elif choice == '8':
            break
        else:
            View.display_message("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
