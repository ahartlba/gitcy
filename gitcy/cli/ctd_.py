from argparse import ArgumentParser
from gitcy import commit_with_title_and_description
from gitcy.core.push import git_push


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "-t",
        "--title",
        required=True,
        type=str,
        help="Commit title (main commit msg)",
    )
    parser.add_argument(
        "-d",
        "--description",
        required=False,
        default=None,
        type=str,
        help="Description ... Additional Information",
    )
    parser.add_argument(
        "-p",
        "--push",
        required=False,
        action="store_true",
        help="Directly push commit",
    )
    args = parser.parse_args()
    commit_with_title_and_description(args.title, args.description)
    if args.push:
        git_push()


if __name__ == "__main__":
    main()
