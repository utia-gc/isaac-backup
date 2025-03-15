import argparse
from importlib.metadata import version as _version
import sys


def version(args: argparse.Namespace) -> None:
    """Print version number and exit
    """
    _ = args

    print(_version("isaac_backup"))
    sys.exit(0)
