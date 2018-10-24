import utility


class Command:
    def exec(self):
        lines = ["bash.py", "", "Developed by Rene (@rmcproductions)", "GNU General Public License v3.0", ""]
        contributors = ["List of all contributors:", "@rmcproductions", "@G3bE", "@Stupremee", "@romangraef"] # Feel free to add your name here
        utility.print_lines_delay(lines + contributors)

    name = "about"
    description = "Shows info about the program and its contributors."
