import os
import platform
import shlex


class Commands:
    import commands

    os.environ['directory'] = os.curdir

    def __init__(self):
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
                    command = getattr(self.commands, invoke)
                except AttributeError:
                    print(invoke + ": Command not found")
                    continue
                command.Command.exec(args)


if __name__ == '__main__':
    commandclass = Commands()
