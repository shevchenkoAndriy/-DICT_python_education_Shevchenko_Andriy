class MarkdownEditor:

    def __init__(self):
        ...

    available_formatters = ("plain", "bold", "italic", "header",
                            "link", "inline-code", "ordered",
                            "list", "unordered-list", "new-line")

    special_commands = "!help", "!done"

    all_commands = (*available_formatters, *special_commands)

    def show_help(self):
        print("Available formatters:", *self.available_formatters)
        print("Special commands:", *self.special_commands)

    def correctly_input_command(self, string):
        user_input = input(string)
        while user_input not in self.all_commands:
            print("Unknown formatting type or command")
            user_input = input(string)
        return user_input

    def menu_options(self):
        option = self.correctly_input_command("Choose a formatter: > ")
        if option == "!help":
            self.show_help()
            self.menu_options()
        elif option == "!done":
            return


mde = MarkdownEditor()
mde.menu_options()
