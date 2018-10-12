class Command:
    """Still hardcoded too. I'm working on this."""

    def exec(self):
        command_list = [["exit", "exits the console"], ["ls", "lists all files in the current directory"], ["cd", "changes the current directory"], ["about", "shows some info about bash.py"], ["help", "shows this list"]]

        for elem in command_list:
            print(elem[0] + "\t" + elem[1])
