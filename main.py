import os
import platform
import shlex
import urllib.request
import json


class Commands:
    import commands

    os.environ['directory'] = "/"

    def __init__(self):
        try:
            commit = json.loads(urllib.request.urlopen("http://api.github.com/repos/rmcproductions/bash.py/commits").read())[0]['commit']
        except Exception:
            commit = {
                "message": "GitHub Connection failed",
                "author": {
                    "name": "unknown"
                }
            }
        print("""
      _               _                   
     | |             | |                  
     | |__   __ _ ___| |__    _ __  _   _ 
     | '_ \ / _` / __| '_ \  | '_ \| | | |
     | |_) | (_| \__ \ | | |_| |_) | |_| |
     |_.__/ \__,_|___/_| |_(_) .__/ \__, |
                             | |     __/ |
     welcome to bash.py!     |_|    |___/ 
     
     Latest commit: """ + str(commit['message']) + """
                by: """ + str(commit['author']['name']) + """

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
