import sys
import time


def printLines(lines):
    for line in lines:
        for i in range(len(line) + 1):
            sys.stdout.write('\r' + line[:i])
            time.sleep(.05)
        time.sleep(.2)
        sys.stdout.write("\n")
