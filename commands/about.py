import utility
import urllib.request
import json


class Command:
    def exec(self):
        lines = ["bash.py", "", "Developed by Rene V. (@rmcproductions)", "GNU General Public License v3.0", ""]
        contents = json.loads(urllib.request.urlopen("http://api.github.com/repos/rmcproductions/bash.py/contributors").read())
        contributors = ["List of all contributors:"]
        for i in contents:
            contributors.append(i['login'])
        utility.print_lines_delay(lines + contributors)

    name = "about"
    description = "Shows info about the program and its contributors."
