import utility


class Command:
    def exec(self):
        lines = ["bash.py", "", "Developed by Rene (@rmcproductions)", "GNU General Public License v3.0"]
        utility.print_lines_delay(lines)
