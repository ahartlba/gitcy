from argparse import ArgumentParser
from pathlib import Path
from typing import Tuple, Sequence, List
from gitcy import commit_with_title_and_description
from gitcy.core.push import push
from gitcy.core.add import add

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
    parser.add_argument(
        "-f",
        "--files",
        required=False,
        nargs='+',
        help="Add files to push",
    )
    parser.add_argument(
        "-a",
        "--all",
        required=False,
        action='store_true',
        help="Add all files",
    )
    args = parser.parse_args()
    if args.all:
        args.files = ['.']

    files_to_add = [Path(a).resolve() for a in args.files]
    valid_files, invalid_files = validate_files(files_to_add)

    if len(invalid_files) > 0:
        inv_filenames = ' '.join(invalid_files)
        print(f'Files {inv_filenames} not found!')
    add(*valid_files)

    commit_with_title_and_description(args.title, args.description)
    if args.push:
        push()

def validate_files(files_to_add: Sequence[str]) -> Tuple[List[str], List[str]]: 
    valid_files = [str(a) for a in filter(lambda x: x.exists(), files_to_add)]
    invalid_files = [str(a) for a in filter(lambda x: (not x.exists()), files_to_add)]
    return valid_files, invalid_files



if __name__ == "__main__":
    main()
