"""Send greetings."""

import arrow
import sys


def pypg(name: str):
    """Hello World."""
    return f"Hello: {name}"


def cli(args=None):
    """Process command line arguments."""
    if not args:
        args = sys.argv[1:]    
    tz = args[0]
    print(pypg(tz))