import os
import platform
import shlex


class Commands:
    """Yes, this is hard-coded. I am still learning."""
    from commands import rm
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
    userin = ""
    while userin != "exit":
        userin = input(platform.uname()[0] + "@" + platform.uname()[1] + os.environ['directory'] + "$ ")

        userin = shlex.split(userin)
        if len(userin) > 0:
            invoke, *args = userin

            try:
                command = getattr(Commands, invoke)
            except AttributeError:
                print(invoke + ": Command not found")
                continue
            command.Command.exec(args)


if __name__ == '__main__':
    __init__()
