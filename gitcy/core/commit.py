import subprocess
from typing import Optional


def commit_with_title_and_description(title: str, description: Optional[str] = None) -> None:
    if description:
        msg = "\n\n".join((title, description))
    else:
        msg = title
    commit(msg)


def commit(msg: str, /) -> None:
    """wrapper for git commit command

    Parameters
    ----------
    msg : str
        commit-message
    """
    subprocess.run(f'git commit -m "{msg}"')
