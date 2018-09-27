import os


class command:
    def exec(args):
        for file in os.listdir(os.environ['directory']):
            print(file)
