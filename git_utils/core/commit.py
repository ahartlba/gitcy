import subprocess
from typing import Optional


def commit_with_title_and_description(title: str, description: Optional[str] = None) -> int:
    if description:
        commit_msg = "\n\n".join((title, description))
    else:
        commit_msg = title
    subprocess.run(f"git commit -m {commit_msg}")
