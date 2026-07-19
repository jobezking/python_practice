# Git Study Guide

## Setup

```bash
git config --global user.email "me@example.com"
git config --global user.name "My name"
```

## Example Session

```bash
mkdir checks
cd checks
git init

ls -la
ls -l
ls -l .git/

cp ../disk_usage.py .
ls -l

git add disk_usage.py
git status

git commit
```

```bash
cd checks
ls -l

git status
```

```bash
kate disk_usage.py
git status

git commit -m 'Add periods to the end of sentences.'
git status
```

```bash
mkdir scripts
cd scripts
git init        # Initialized empty Git repository in /home/user/scripts/.git/

git config -l
```

### Sample code: `all_checks.py`

```python
#!/usr/bin/env python3

def main():
    pass

main()
```

```bash
chmod +x all_checks.py
git status

git add all_checks.py
git commit
```

### Updated file

```python
#!/usr/bin/env python3

import os

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def main():
    pass

main()
```

```bash
git status
git add all_checks.py
git status
git commit -m 'Add a check_reboot function'
```

## Summary

In any Git project, there are three sections: the **Git directory**, the **working tree**, and the **staging area**. This study guide provides some basic concepts and commands that can help you get started with Git, as well as guidelines to help you write an effective commit message.

## Core Commands

### `git config`

The `git config` command is used to set the values that identify who made changes to Git repositories. To set the values of `user.email` and `user.name` to your email and name, type:

```bash
git config --global user.email "me@example.com"
git config --global user.name "My name"
```

### `git init`

```bash
git init
```

The `git init` command can create a new empty repository in the current directory, or re-initialize an existing one.

### `ls -la`

```bash
ls -la
```

Checks that an identified directory exists.

```bash
ls -l .git/
```

Checks inside the directory to see the different things that it contains. This is called the **Git directory**. The Git directory is a database for your Git project that stores the changes and the change history.

### `git add`

```bash
git add disk_usage.py
```

Allows Git to track your file and uses the selected file as a parameter when adding it to the staging area. The **staging area** is a file maintained by Git that contains all the information about what files and changes are going to go into your next commit.

### `git status`

```bash
git status
```

Used to get information about the current working tree and pending changes.

### `git commit`

```bash
git commit
```

Moves changes from the staging area to the `.git` directory. Running this command tells Git to save changes. A text editor opens, allowing a commit message to be entered.

## Guidelines for Writing Commit Messages

A commit message is generally broken into two sections: a short summary and a description of the changes. When `git commit` is run, Git opens a text editor for the commit message. A good commit message includes:

- **Summary** — The first line, formatted as a header, containing 50 characters or less.
- **Description** — Usually kept under 72 characters per line, providing detailed information about the change. It can include references to bugs or issues fixed by the change, and links to more information when relevant.

See an example commit message at [commit.style](https://commit.style/).

## Key Takeaways

Knowing basic Git commands and guidelines for writing better commit messages can help you get started with Git, and helps you communicate more effectively with others.
