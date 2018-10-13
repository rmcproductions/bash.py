from .rm import *
from .help import *
from .exit import *
from .cd import *
from .ls import *
from .about import *
from .inbuild import *

commands = [
    rm.Command,
    help.Command,
    exit.Command,
    cd.Command,
    ls.Command,
    about.Command,
    inbuild.Command
]
