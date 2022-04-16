# create-branch-based-on-commit-message

## What is solves?

Everybody that uses branches for Code Review (or Pull Request/ Merge Request) has to choose *how to name* that branch.

This script creates branch name based on commit message with "some" convention.

BTW it is also good to have any convention for branch names in your team (company).

## How it works?

Takes the last commit message and checkouts to new branch.

Some examples how the commit message is transformed to branch name

| Commit message | | Branch name |
| ----------- | ----------- | ----------- |
| `"feat: #OLDM-324 create product endpoint"` | &rarr; | `"feat/OLDM-324/create-product-endpoint"` |
| `"fix: fix email"` | &rarr; | `"fix/fix-email"` |
| `"add new TODO"` | &rarr; | `"add-new-todo"` |

## How to use

### Prerequisites

**Python** have to be installed on your machine (unless somebody will rewrite tiny script to bash)

### Unix/Mac users

* Copy files `to_branch` and `parsing.py` to your `/usr/local/bin` folder
* make it executable `chmod u+x /usr/local/bin/to_branch`
* run `to_branch` in your repository
