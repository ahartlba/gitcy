import subprocess

def add(*files):
    """files to add to git"""

    if len(files) == 0:
        return
    if len(files) == 1:
        subprocess.run(f'git add {files[0]}')

    files_ = ' '.join(files)
    subprocess.run(f'git add {files_}')
