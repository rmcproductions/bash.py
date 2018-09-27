import os
import platform

class commands:
    from commands import help
    from commands import exit
    from commands import cd
    from commands import ls


os.environ['directory'] = "/"


def __init__():
    username = "admin"
    userin = ""
    while userin != "exit":
        userin = input( platform.uname()[0] + "@" + platform.uname()[1] + os.environ['directory'] + "$ ")

        userin  = userin.split(" ")
        invoke  = userin[0]
        args    = userin[1:]

        global commands
        if hasattr(commands, invoke):
            getattr(commands, invoke).command.exec(args)
        else:
            print(invoke + ": Command not found")


__init__()
