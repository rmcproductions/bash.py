import os
import time
import sys


class Command:
    def exec(args):
        for file in os.listdir(os.environ['directory']):
            sys.stdout.flush()
            print(file)
            if "slow" in args:
                time.sleep(.1)
