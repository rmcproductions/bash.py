import time
import sys


class command:
    def exec(self):
        lines = ["bash.py", "", "Developed by Rene (@rmcproductions)", "GNU General Public License v3.0"]
        for line in lines:
            for i in range(len(line) + 1):
                sys.stdout.write('\r' + line[:i])
                time.sleep(.05)
            sys.stdout.write("\n")
