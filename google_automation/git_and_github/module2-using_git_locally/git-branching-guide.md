# Git Branching Exercise & Study Guide

## Section 1: Example Session

```bash
git branch
git merge even-better-feature
git log

kate free_memory.py
#!/usr/bin/env python3

def main():
    """Checks if there's enough free memory in the computer."""

main()

git commit -a -m 'Add comment to main()'

git checkout even-better-feature

kate free_memory.py
#!/usr/bin/env python3

def main():
    print("Everything ok.")

main()

git commit -a -m 'Print everything ok'
git checkout master
git merge even-better-feature  # fails because of uncommitted files
git status

git add free_memory.py
git status
git commit

git log --graph --oneline
```

## Section 2: Git Branching Study Guide

Now that you've learned about branches and merging, use this study guide as an easy reference for Git branching. This study guide gives a brief explanation of these useful commands along with a link to the Git documentation for each command. Keeping study guides like this one easily accessible can help you code more efficiently.

| Command | Explanation & Link |
|---|---|
| `git branch` | `$ git branch` can be used to list, create, or delete branches. |
| `git branch <name>` | `$ git branch <name>` can be used to create a new branch in your repository. |
| `git branch -d <name>` | `$ git branch -d <name>` can be used to delete a branch from your repository. |
| `git branch -D <name>` | `$ git branch -D <branch>` forces a branch to be deleted. |
| `git checkout <branch>` | `$ git checkout <branch>` switches your current working branch. |
| `git checkout -b <new-branch>` | `$ git checkout -b <new-branch>` creates a new branch and makes it your current working branch. |
| `git merge <branch>` | `$ git merge <branch>` joins changes from one branch into another branch. |
| `git merge --abort` | `$ git merge --abort` can only be used after merge conflicts. This command will abort the merge and try to go back to the pre-merge state. |
| `git log --graph` | `$ git log --graph` prints an ASCII graph of the commit and merge history. |
| `git log --oneline` | `$ git log --oneline` prints each commit on a single line. |

Keep this table handy while you are getting comfortable using Git branches and merging. Now, it's time to put your newfound knowledge of Git branches and merging to use!

Terms and definitions from Course 3, Module 2
Branch: A pointer to a particular commit, representing an independent line of development in a project

Commit ID: An identifier next to the word commit in the log

Fast-forward merge: A merge when all the commits in the checked out branch are also in the branch that's being merged

Head: This points to the top of the branch that is being used

Master: The default branch that Git creates for when a new repository initialized, commonly used to place the approved pieces of a project

Merge conflict: This occurs when the changes are made on the same part of the same file, and Git won't know how to merge those changes

Rollback: The act of reverting changes made to software to a previous state 

Three-way merge: A merge when the snapshots at the two branch tips with the most recent common ancestor, the commit before the divergence