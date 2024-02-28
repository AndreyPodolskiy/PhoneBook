
class TextMessages:
    @staticmethod
    def menu():
        return """
        Телефонная книга. Выберите действие:
        1. Открыть справочник
        2. Сохранить справочник
        3. Показать все контакты
        4. Создать контакт
        5. Найти контакт
        6. Изменить контакт
        7. Удалить контакт
        8. Выход
        """

    @staticmethod
    def input_contact():
        return "Введите контакт в формате 'Имя - Номер телефона': "

    @staticmethod
    def input_name():
        return "Введите имя контакта: "

    @staticmethod
    def input_new_contact():
        return "Введите новый контакт в формате 'Имя - Номер телефона': "

    @staticmethod
    def input_old_contact():
        return "Введите существующий контакт для обновления: "
