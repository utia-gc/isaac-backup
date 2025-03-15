from .cli import get_args


def main() -> None:
    """Main program logic
    """
    args = get_args()

    args.func(args)


if __name__ == "__main__":
    main()
