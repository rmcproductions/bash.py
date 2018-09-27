import os


class command:
    def exec(args):
        if args[0] == "..":
            os.environ['directory'] = "/".join(os.environ['directory'].split("/")[:-2])
            if os.environ['directory'] == "":
                os.environ['directory'] = "/"
        elif " ".join(args[:]) in os.listdir(os.environ['directory']):
            os.environ['directory'] = os.environ['directory'] + " ".join(args[:]) + "/"
        else:
            print(" ".join(args[:]) + ": Directory doesn't exist")
