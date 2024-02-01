from Bot import Bot


def main():
    print('Hello. I am your contact-assistant. What should I do with your contacts?')
    bot = Bot()
    bot.book.load("auto_save")
    commands = ['Add', 'Search', 'Edit', 'Load', 'Remove', 'Save', 'Congratulate', 'View', 'Exit']
    while True:
        try:
            action = input('Type help for list of commands or enter your command\n').strip().lower()
            if action == 'help':
                format_str = str('{:%s%d}' % ('^', 20))
                for command in commands:
                    print(format_str.format(command))
                action = input().strip().lower()
                bot.handle(action)
                if action in ['add', 'remove', 'edit']:
                    bot.book.save("auto_save")
            else:
                bot.handle(action)
                if action in ['add', 'remove', 'edit']:
                    bot.book.save("auto_save")
            if action == 'exit':
                break
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting...")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
