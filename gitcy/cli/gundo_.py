from argparse import ArgumentParser
from gitcy.core.undo import undo_last_commit


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "mode",
        type=str,
        default='',
        nargs='?',
        choices=['', 'soft', 'hard'],
        help="Mode of undo: either '', 'soft' or 'hard'",
    )
    args = parser.parse_args()
    undo_last_commit(args.mode)


if __name__ == "__main__":
    main()
