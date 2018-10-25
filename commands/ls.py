import os
import time
import sys
import utility


class Command:
    def exec(args):
        directories = []
        files = []

        print("Listing files and directories for " + os.path.dirname(os.environ['directory']) + "...")

        for file in os.listdir(os.environ['directory']):
            sys.stdout.flush()

            if os.path.isfile(os.environ['directory'] + file):
                files.append([os.path.getsize(os.environ['directory'] + file), file])
            else:
                directories.append(file)
                
        for i in directories:
            print("DIR\t\t" + i)
            if "slow" in args:
                time.sleep(.1)
        for i in files:
            print("FILE\t" + utility.norm_file_size(i[0]) + "\t" + i[1])
            if "slow" in args:
                time.sleep(.1)



    name = "ls"
    description = "Shows a list of all files and folders in the current directory."
