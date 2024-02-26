from argparse import ArgumentParser
from git_utils import commit_with_title_and_description
from git_utils.core.push import git_push


def main():
    parser = ArgumentParser()
    parser.add_argument("-t", "--title", required=True, type=str)
    parser.add_argument("-d", "--description", required=False, default=None, type=str)
    parser.add_argument("-p", "--push", required=False, action="store_true")
    args = parser.parse_args()
    commit_with_title_and_description(args.title, args.description)
    if args.push:
        git_push()


if __name__ == "__main__":
    main()
