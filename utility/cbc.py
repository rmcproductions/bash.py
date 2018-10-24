import sys
import time


def print_lines_delay(lines, delay = .05):
    for line in lines:
        for i in range(len(line) + 1):
            sys.stdout.write('\r' + line[:i])
            time.sleep(delay)
        time.sleep(delay * 4)
        sys.stdout.write("\n")
