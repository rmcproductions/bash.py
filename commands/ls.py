import os
import time
import sys


class Command:
    def exec(args):
        directories = []
        files = []

        for file in os.listdir(os.environ['directory']):
            sys.stdout.flush()

            if os.path.isfile(os.environ['directory'] + file):
                files.append(file)
            else:
                directories.append(file)
                
        for i in directories:
            print("DIR\t" + i)
        for i in files:
            print("FILE\t" + i)
            if "slow" in args:
                time.sleep(.1)

    name = "ls"
    description = "Shows a list of all files and folders in the current directory."
