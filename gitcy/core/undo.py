import subprocess
from typing import Optional

def undo_last_commit(mode: Optional[str] = None):
    if mode is None:
        mode = ''
    if mode not in ('', 'hard', 'soft'):
        raise ValueError(f"Mode has to be either ('', 'hard', 'soft') but is {mode}")
    if mode:
        cmd = f'git reset --{mode} HEAD~1'
    else:
        cmd = 'git reset HEAD~1'
    subprocess.run(cmd)
