class MarkdownEditor:

    def __init__(self):
        self.selected_format = None
        self.content = ""
        self.on_help_message = True
    test_string = """
# Simple Editor


## About the project

Hi, this App will help you add Markdown markup through the console. 

## Usage example

```if option == "ordered-list":```
1. text option   
    1.1 plain  
    1.2 bold  
    1.3 italic  
2. header  
3. link  
4. inline-code
5. list option  
    * ordered-list  
    * unordered-list  
6. new-line  
  
```if option == "unordered-list":```  
* !help  
* !done  
  
```if option == "bold":```  

**bold**

```if option == "italic":```  

*italic*"""

    reserved_characters = ("*", "**", "```", "#")

    available_formatters = ("plain", "bold", "italic", "header",
                            "link", "inline-code", "ordered-list",
                            "unordered-list", "new-line")

    special_commands = "!help", "!done"

    all_commands = (*available_formatters, *special_commands)

    def show_help(self):
        print("Available formatters:", *self.available_formatters)
        print("Special commands:", *self.special_commands)

    def correctly_input_command(self, string):
        user_input = input(string)
        while user_input not in self.all_commands:
            if not user_input:
                print("If you do not know what to do write command !help")
                user_input = input(string)
                continue
            print("Unknown formatting type or command")
            user_input = input(string)
        return user_input

    def menu_options(self):
        option = self.correctly_input_command("Choose a formatter: > ")
        if option == "!help":
            self.show_help()
            self.menu_options()

        elif option == "!done":
            self.add_markup(self.content)
            return

        elif option == "plain":
            user_input = self.correct_input("Text: > ")
            self.content += f"{user_input} "

        elif option == "bold":
            user_input = self.correct_input("Text: > ")
            self.content += f"**{user_input}** "

        elif option == "italic":
            user_input = self.correct_input("Text: > ")
            self.content += f"*{user_input}* "

        elif option == "header":
            level = self.correct_input_level("Level: > ")
            user_input = self.correct_input("Text: > ")

            if not self.selected_format:
                self.content += f"\n"
                self.selected_format = option
            else:
                self.content += f"\n\n"

            self.content += f"{level * '#'} {user_input}\n\n"

        elif option == "link":
            label = self.correct_input("Label: > ")
            url = self.correct_input("URL: > ")
            self.content += f"[{label}]({url}) "

        elif option == "inline-code":
            user_input = self.correct_input("Text: > ")
            self.content += f"```{user_input}``` "

        elif option == "ordered-list":
            self.add_list("ordered")

        elif option == "unordered-list":
            self.add_list("unordered")

        elif option == "new-line":
            self.content += "  \n"

        print(self.content)
        self.menu_options()

    def add_list(self, type):
        number_rows = self.input_number_rows("Number of rows: > ")
        for row in range(1, number_rows + 1):
            self.create_list_item(row, type)

    def add_nested_list(self, type, prev_row):
        number_rows = self.input_number_rows("Number of rows: > ")
        for row in range(1, number_rows + 1):
            current_row = f"{prev_row}.{row}"
            self.create_nested_item(current_row, type)

    def nested_lists(self, row):
        option = input("""        
        
Select the type:
1: ordered-list
2: unordered-list

     Enter [exit] 
> """)
        if option == "":
            return
        if option == "1":
            self.add_nested_list("ordered-nested", row)
        elif option == "2":
            self.add_nested_list("unordered-nested", row)
        else:
            print("Error command, try again ")
            self.nested_lists(row)

    def create_list_item(self, row, type):
        number_item = row
        user_input = self.correct_input(f"Row #{row}: > ")
        if row + 1 != 1 and self.on_help_message:
            print("""
                        You can add a nested list if you like
                                                  Enter [add]""")
            self.on_help_message = False

        if user_input == "":
            number_item -= 1
            self.nested_lists(number_item)
            self.create_list_item(row, type)
            return
        if type == "ordered":
            self.content += f"{row}. {user_input}  \n"
        elif type == "unordered":
            self.content += f"* {user_input}  \n"

    def create_nested_item(self, row, type):
        margin = "    "
        user_input = self.correct_input(f"{margin}Row #{row}: > ")
        if user_input == "":
            print("Nested list are not available here")
            self.create_nested_item(row, type)
            return
        if type == "ordered-nested":

            self.content += f"{margin}{row} {user_input}  \n"

        elif type == "unordered-nested":

            self.content += f"{margin}* {user_input}  \n"

    def correct_input(self, string):
        user_input = input(string)
        while not set(self.reserved_characters).isdisjoint(user_input):
            print("Sorry, these characters are not allowed here:",
                  *self.reserved_characters)
            user_input = input(string)
        return user_input

    @staticmethod
    def correct_input_level(string):
        user_input = input(string)
        while user_input:
            try:
                user_input = int(user_input)
            except ValueError:
                print("Please input number")
                user_input = input(string)
                continue

            else:
                user_input = int(user_input)
                if not 0 < user_input <= 6:
                    print("The level should be within the range of 1 to 6.")
                    user_input = input(string)
                    continue
                break

        return user_input

    @staticmethod
    def input_number_rows(string):
        user_input = input(string)
        while user_input:
            try:
                user_input = int(user_input)
            except ValueError:
                print("Please input number")
                user_input = input(string)
                continue

            else:
                user_input = int(user_input)
                if not 0 < user_input:
                    print("Number rows cannot be negative")
                    user_input = input(string)
                    continue
                break

        return user_input

    @staticmethod
    def add_markup(content):
        file = open("output.md", "w")
        file.write(content)
        file.close()
        print("Save successfully")


mde = MarkdownEditor()
# mde.menu_options()
mde.add_markup(mde.test_string)
