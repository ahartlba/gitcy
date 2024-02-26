import subprocess
from typing import Optional

def ctd(title: str, description: Optional[str] = None) -> int:
  if description:
    commit_msg = "\n\n".join((title, despcription))
  else:
    commit_msg = title
  try:
    subprocess.run(f"git commit -m {commit_msg}")
    return 0
  except Exception as e:
    print(f"Expception {e} occured while trying to commit {commit_msg}")
  return -1

if __name__ == '__main__':
  from argparse import ArgumentParser
  parser = ArgumentParser()
  parser.add_argument('-t', '--title', required=True, type=str)
  parser.add_argument('-d', '--description', required=False, default=None, type=str)
  args = parser.parse_args()
  return ctd(args.title, args.description)  # return status code
  
