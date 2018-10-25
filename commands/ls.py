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
                files.append([os.path.getsize(os.environ['directory'] + file), file])
            else:
                directories.append(file)
                
        for i in directories:
            print("DIR\t" + i)
        for i in files:
            if i[0]/1e+6 <= 1000 and i[0]/1e+3 < 100000:
                print("FILE\t" + str(round(i[0]/1e+3)) + "kB\t" + i[1])
            elif i[0]/1e+6 >= 1000:
                print("FILE\t" + str(round(i[0]/1e+9)) + "GB\t" + i[1])
            else:
                print("FILE\t" + str(round(i[0]/1e+6)) + "MB\t" + i[1])

            if "slow" in args:
                time.sleep(.1)

    name = "ls"
    description = "Shows a list of all files and folders in the current directory."
