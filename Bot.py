from AddressBook import AddressBook
from consoleinterface import ConsoleInterface


class Bot:
    def __init__(self):
        self.book = AddressBook()
        self.ui = ConsoleInterface()

    def handle(self, action, success=None, display_search_results=None, display_congratulations=None):
        if action == 'add':
            name = self.ui.get_user_input("Name: ").strip()
            phones = self.ui.get_user_input("Phones (+48......... or +38..........): ")
            birth = self.ui.get_user_input("Birthday date (dd/mm/YYYY): ")
            email = self.ui.get_user_input("Email: ").strip()
            status = self.ui.get_user_input("Type of relationship (family, friend, work): ").strip()
            note = self.ui.get_user_input("Note: ")
            record = self.book.create_record(name, phones, birth, email, status, note)
            self.book.add(record)
            self.ui.display_message(f"Contact {name} has been added.")
        elif action == 'search':
            category = self.ui.get_user_input("Search category: ")
            pattern = self.ui.get_user_input("Search pattern: ")
            result = self.book.search(pattern, category)
            display_search_results(result)
        elif action == 'edit':
            contact_name = self.ui.get_user_input("Contact name: ")
            parameter = self.ui.get_user_input(
                "Which parameter to edit (name, phones, birthday, status, email, note): ").strip()
            new_value = self.ui.get_user_input("New Value: ")
            success = self.book.edit(contact_name, parameter, new_value)
            if success:
                self.ui.display_message(f"Contact {contact_name} has been edited!")
            else:
                self.ui.display_message(f"There is no such contact in the address book!")
        elif action == 'remove':
            pattern = self.ui.get_user_input("Remove (contact name or phone): ")
            self.book.remove(pattern)
            if success:
                self.ui.display_message(f"Contact {pattern} has been removed!")
            else:
                self.ui.display_message(f"There is no such contact in the address book!")
        elif action == 'save':
            file_name = self.ui.get_user_input("File name: ")
            self.book.save(file_name)
            self.ui.display_message("Address book has been saved!")
        elif action == 'load':
            file_name = self.ui.get_user_input("File name: ")
            self.book.load(file_name)
            self.ui.display_message("Address book has been loaded!")
        elif action == 'congratulate':
            display_congratulations(self.book.congratulate())
        elif action == 'view':
            self.ui.display_address_book(self.book)
        elif action == 'exit':
            pass
        else:
            self.ui.display_message("There is no such command!")
