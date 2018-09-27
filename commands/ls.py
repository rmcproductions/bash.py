import os
import time
from utility import cbc


class command:
    def exec(args):
        print()
        print("Objects in " + os.environ['directory'])
        for file in os.scandir(os.environ['directory']):
            if file:
                print("FILE\t" + file.name)
            else:
                print("DIR\t" + file.name)
            if "slow" in args:
                time.sleep(.1)
