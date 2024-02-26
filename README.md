# Gitcy

A small python package for some github cli utilities.
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

## Install

Use either pipx to install

```shell
pipx install git+https://github.com/ahartlba/gitcy.git
```

or install the package in your python environment and use it there.

```shell
pip install gitcy
```
