import utility
import urllib.request
import json


class Command:
    def exec(self):
        lines = ["bash.py", "", "Developed by Rene V. (@rmcproductions)", "GNU General Public License v3.0", ""]
        contributors = ["List of all contributors:"]
        contents = 0
        try:
            contents = json.loads(urllib.request.urlopen("http://api.github.com/repos/rmcproductions/bash.py/contributors").read())
            for i in contents:
                contributors.append(str(i['contributions']) + " commits\t" + i['login'])
        except Exception:
            contributors = ["Automatic getting of contributors failed. check your connection."]
        utility.print_lines_delay(lines + contributors)

    name = "about"
    description = "Shows info about the program and its contributors."
