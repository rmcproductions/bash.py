import os
import platform
from utility import cbc


class Command:
    def exec(self):
        print('Everything you type, will be given to the normal OS shell; type \'exit\' to exit this mode.')
        userin = input(platform.uname()[0] + "@" + platform.uname()[1] + os.environ['directory'] + "$ ")
        while userin != 'exit':
            output = os.popen(userin).readlines()
            cbc.print_lines(output)
            userin = input(platform.uname()[0] + "@" + platform.uname()[1] + os.environ['directory'] + "$ ")
