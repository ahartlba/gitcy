# Gitcy

A lightweight python package for some github cli utilities.

Is it necessary? No.

Is it helpful? Maybe.

Does it feel better? Yes.

## Why

Instead of writing

```shell
git commit -m "Title \n\nMore Description"
git push
```

you can directly type

```shell
ctd -t "Title" -d "More Description" -p
```

or even select the files to stage before commiting

```shell
ctd -t "Title" -d "More Description" -f 'module/test.py' -p
```

of stage all files before comiting (be carefull though :))

```shell
ctd -t "Title" -d "More Description" -p --all
```

## Install

Use either pipx to install

```shell
pipx install git+https://github.com/ahartlba/gitcy.git
```

or install the package in your python environment and use it there.

```shell
pip install gitcy
```

## Commands

- ``ctd`` stands for Commit with Title and Description. Add title and additional description to your commit-msg. Additionally select files and push in one command
- ``gundo`` stands for gitcy undo ... which undoes last commit
