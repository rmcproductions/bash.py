import os
import platform

"""Yes, this is hard-coded. I am still learning."""
class commands:
    from commands import help
    from commands import exit
    from commands import cd
    from commands import ls
    from commands import about


os.environ['directory'] = "/"


def __init__():
    print("""
  _               _                   
 | |             | |                  
 | |__   __ _ ___| |__    _ __  _   _ 
 | '_ \ / _` / __| '_ \  | '_ \| | | |
 | |_) | (_| \__ \ | | |_| |_) | |_| |
 |_.__/ \__,_|___/_| |_(_) .__/ \__, |
                         | |     __/ |
 welcome to bash.py!     |_|    |___/ 
 
 For a list of all commands, type 'help'
""")
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
