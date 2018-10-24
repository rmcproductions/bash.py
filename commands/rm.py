import os


class Command:
    def exec(args):
        if len(args) == 0:
            return

        path = os.path.join(os.environ['directory'], " ".join(args[:]))
        if os.path.isfile(path):
            os.remove(path)
        else:
            print(f"rm: Cannot remove {path}: It´s a directory")

    name = "rm"
    description = "Deletes a file from the current directory."
