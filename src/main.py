import argparse
import sys


def main() -> None:
    """Main program logic
    """
    args = get_args()

    if args.verbose:
        print(f"Command: {args.command}")

    args.func(args)


def get_args() -> argparse.Namespace:
    """Get command line arguments

    :return: Parsed arguments
    :rtype: argparse.Namespace
    """
    parser = argparse.ArgumentParser(
        description="Convenience utilities for backups on ISAAC."
    )
    # add subcommands
    subparsers = parser.add_subparsers(dest="command", help="Command to execute.")

    # add global arguments
    parser.add_argument("-v", "--verbose", action="store_true", help="Print additional output.")

    # create parser for `version` command
    parser_version = subparsers.add_parser("version", help="Print program version number and exit")
    parser_version.set_defaults(func=version)

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(0)

    return args


def version(args: argparse.Namespace) -> None:
    """Print version number and exit
    """
    _ = args

    print("v0.0.0.9000")
    sys.exit(0)


if __name__ == "__main__":
    main()
