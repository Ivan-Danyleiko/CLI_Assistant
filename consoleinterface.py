from userinterface import UserInterface


def display_search_results(result):
    for account in result:
        if account['birthday']:
            birth = account['birthday'].strftime("%d/%m/%Y")
            result = "_" * 50 + "\n" + (
                    f"Name: {account['name']} \nPhones: {', '.join(account['phones'])}"
                    f"\nBirthday: {birth} \nEmail: {account['email']} "
                    f"\nStatus: {account['status']} \nNote: {account['note']}\n") + "_" * 50
            print(result)


def display_congratulations(param):
    print(param)


class ConsoleInterface(UserInterface):
    def display_contacts(self, contacts):
        for contact in contacts:
            print(f"Name: {contact['name']}")
            print(f"Phones: {', '.join(contact['phones'])}")
            print(f"Birthday: {contact['birthday'].strftime('%d/%m/%Y')}")
            print(f"Email: {contact['email']}")
            print(f"Status: {contact['status']}")
            print(f"Note: {contact['note']}")
            print("_" * 50)

    def display_notes(self, notes):
        for note in notes:
            print(f"Note: {note}")
            print("_" * 50)

    def display_commands(self, commands):
        format_str = str('{:%s%d}' % ('^', 20))
        for command in commands:
            print(format_str.format(command))

    @staticmethod
    def get_user_input(param):
        return input(param)

    @staticmethod
    def display_message(param):
        print(param)

    def display_address_book(self, book):
        contacts = book.data
        if not contacts:
            print("The address book is empty.")
        else:
            self.display_contacts(contacts)
