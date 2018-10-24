import utility
import commands

class Command:

    def exec(self):
        for i in commands.commands:
            print(i.name + "\t" +i.description)

    name = "help"
    description = "Shows a list of all commands."
