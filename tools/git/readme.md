# Git

How to use git successfully even with a little background knowledge.

## Basic Information

Git is a version control system. Probably the best way to learn it is just to read the [documentation](https://git-scm.com/doc). In case you do not have much time and just need to jump on the train, this document helps you to understand the basics fast.

Git keeps the versions as a snapshots on your local machine. It enables you to work completely offline and synchronize the code with the remote repository when it suits you.

**There are four levels in the git hierarchy**

| Git Levels        | Description                                                        |
| ---               | ---                                                                |
| Working Tree      | The actual files in the local directory managed by git.            |
| Index             | Git structure of the files. Not in index - does not exist for git. |
| Committed         | There is a snapshot version of the files. It can be shared.        |
| Remote Repository | The commit (snapshot) was shared through push or pull with others. |

**In terms of files, they can be in one of three states**

1) Modified: Changes not staged for commit.
    - Some files are either untracked, modified or deleted.
2) Staged: Changes to be committed (recorded in the index).
    - The file changes (e.g. modified, renamed, new file, deleted) are staged for the next commit.
3) Committed: Nothing to commit, working tree clean.
    - Files in the working tree and files in the last commit identical.

## Git Installation and Setup

### Create a Git Account

First step is to create account on some git site such as GitHub, GitLab etc.

* [GitHub - Where the world builds software](https://github.com/)
* [GitLab is the open DevOps platform](https://about.gitlab.com/)

Once you have it, add your public SSH key to it.

### Basic Git Configuration

After the git installation, there is a need of some configurations.

```sh
git config --global user.name "Name Surname"
git config --global user.email "username@email.com"
```

## Basic Commands

| Git Command  | Description                                                |
| ---          | ---                                                        |
| git init     | Create an empty Git repository or reinitialize an existing one. |
| git clone    | Clones remote git repository to your machine as local git repository. |
| git add      | Add file contents to the index.                            |
| git commit   | Record changes to the repository.                          |
| git push     | Pushes local repository to the remote one.                 |
| git fetch    | Downloads content from remote git repository.              |
| git merge    | Incorporates changes from given named branch to current branch. |
| git pull     | Does git fetch and git merge.                              |
| git branch   | Branch is simply a pointer to specific snapshot (version). |
| HEAD         | Special pointer which point at the branch you are currently on. |
| git checkout | Changes branch at which the HEAD is pointing and updates the local files to match with that branch (switch branches). |

### Git --help

Git has a beautifully done manual, so adding `--help` after any command is usually sufficient help once you start using the git.

```sh
# Example of help for rm command
git rm --help
```

### Create a Project (git clone, git init, git fork)

It is either possible to create a new repository (project) or to find some already existing.

**Create repository from scratch**

On your GITSITE create a new repository and get its URL under button "clone" (e.g. https://github.com/USERNAME/PROJECT.git)

```sh
# Clone the repository (project) to your machine
git clone git@YOUR_PROJECT_PATH.git

# Create README.md about your project
echo "# REPOSITORY_NAME" >> README.md #touch README.md
```

**Create repository from existing directory**

```sh
cd EXISTING_DIRECTORY
echo "# REPOSITORY_NAME" >> README.md #touch README.md

# Create an empty Git repository or reinitialize an existing one
git init

# Add remote site git@GITSITE:USER/REPOSITORY.git as origin
git remote add origin git@GITSITE.com:USER_NAME/REPOSITORY_NAME.git
```

* [From github.com](https://github.com/)

**Create a repository from an existing repository**

There is an option to use an existing project as your starting point by making a copy. It is called a fork, by doing so you will have your own copy of the whole project. Then you can just git clone and start doing stuff.

### See Status of the Index (git status)

Files can be either untracked, added, modified or deleted.

```sh
# Show status of git files, which where not added, which were deleted but added etc.
git status
```

### File Changes (Differences) (git diff)

```sh
# Show changes between staged file and file in the working tree.
git diff path/to/file
```

### Stage Changes to the Index (git add, git rm, git mv)

Stage files to the index for the next commit.

```sh
# Add the one file (README.md) to the index (will be commited).
git add README.md

# Add all the files from current directory.
git add .

# Add all files to the index.
git add -A          # git add --all
```

**Remove Files from the Index**

```sh
# Remove files from the working tree and from the index (File is deleted and will not be commited).
git rm FILE
# Delete directory (option recursive).
git rm -r DIR
# Remove FILE only from index (file will not be commited) it doesn't delete it locally.
git rm --cached FILE
# Forced remove - the file is deleted from index and working tree even when it has local modifications.
git rm -f FILE
```

**Rename or move files**

```sh
# Move or rename files.
git mv file/path new/file/path
```

* [git mv (git-scm.com)](https://git-scm.com/docs/git-mv)

**Discard Local Changes**

```
# Discard changes in working directory.
git checkout -- FILENAME
```

### Commit Changes (git commit)

```sh
# Commit (record) the changes with a meaningful message.
git commit -m "Initial commit, README.md created."

# Write commit message in advance to a file and then use it for commit.
git commit -eF commit_message.txt

# Redo last commit with new changes
git commit --amend
```

* [Preparing a git commit message before committing? (stackoverflow.com)](https://stackoverflow.com/questions/20438293/preparing-a-git-commit-message-before-committing)

### Push Commits to the Remote Repository (git push)

```
# Pushes the current branch to the remote repository called "origin".
git push -u origin

# Pushes local "main" branch to the remote repository called "origin".
git push -u origin main

# Pushes local "main" branch to the "dev" branch of remote repository "origin".
git push origin main:dev

# Forcing push if necessary (rewriting commits history perhaps).
git push -f
```

## Ignore Files from the Git Structure (.gitignore)

`.gitignore` file specifies intentionally untracked files to be ignored.

```.gitignore
# Ignore all .ipynb checkpoints
.ipynb_checkpoints
# Ignore knapsack instances directory
./knapsack/instances
```

* [gitignore (git-scm.com)](https://git-scm.com/docs/gitignore)
* [How to git ignore ipython notebook checkpoints anywhere in repository (stackoverflow.com)](https://stackoverflow.com/questions/35916658/how-to-git-ignore-ipython-notebook-checkpoints-anywhere-in-repository)

## Advanced Commands

### See Commits, Diffs and Messages (git log, git diff, git show)

```sh
# Show all commits of the current branch.
git log

# Show all commits that are fetched, graphically.
git log --all --graph

# Show commits affecting the a specific file (--oneline makes message and commit's hash shorter).
git log --oneline path/to/file.sth

# Diff file with it's version from given commit (commit's hash taken from git log).
git diff 0a42637 path/to/file.sh

# Show information about given commit, tag, etc.
git show 0a42637
```

* [git diff file against its last change (stackoverflow.com)](https://stackoverflow.com/questions/10176601/git-diff-file-against-its-last-change)

### Branching (git branch, git checkout)

The main branch is by default called "main".
In the past, it was often called "master".
Good practise is to create a separate branch for development.

```sh
# Show branches - the current is marked with asterix
git branch

# List all branches, also the remote ones
git branch -a

# Create branch
git branch BRANCH_NAME

# Change to a branch
git checkout BRANCH_NAME

# Change the current branch to main
git checkout main

# Crate branch and check out to it in one step
git checkout -b BRANCH_NAME

# Delete branch
git branch -d BRANCH_NAME

# Remove branches deleted on the remote
git fetch --prune origin
# or
git remote prune origin

# Rename branch
git branch -m NEW_BRANCH_NAME
```

### Merging (git merge)

Merge the ANOTHER_BRANCH to main.

```sh
git checkout main

git merge ANOTHER_BRANCH

# Merge the local content with BRANCH_NAME of REMOTE_NAME
git merge --allow-unrelated-histories REMOTE_NAME/BRANCH_NAME

# No fast-foreward (--no-ff)
git merge --no-ff ANOTHER_BRANCH

# Apply all changes from another branch (then it can be commited in one commit).
git merge --squash ANOTHER_BRANCH
```

* [No fast-foreward - A successful Git branching model (nvie.com)](https://nvie.com/posts/a-successful-git-branching-model/).

### Remote Repositories (git remote)

Once you clone a repository, it sets a remote for the repository under the origin.
Thanks to that you can push your code to origin (the remote repository) or to pull code from the repository.

```sh
# Show the remotes
git remote -v

# Add remote
git remote add NAME URL

# Add remote and fetch
git remote add -f NAME URL

# Delete remote
git remote remove NAME URL

# Set remote url
git remote set-url origin git@github.com:USERNAME/REPOSITORY.git
```

### Download Remote Branch and Test It (git fetch, git checkout)

```sh
# Fetch files from origin( remote site).
git fetch origin

# Create the desired BRANCH_NAME from origin and change to it.
git checkout -b BRANCH_NAME origin/BRANCH_NAME
```

### Pulling - Download from Remote and Merge (git pull)

```sh
# Git pull - equivalent to git fetch and git merge.
git pull

# Fetch origin branch from remote origin( and merge it with local branch origin).
git pull origin main
```

**Git pull using git fetch and git merge.**

```sh
# Downloads content from a remote repository and write to .git/FETCH_HEAD
git fetch
# Merges the FETCH_HEAD to the current branch.
git merge FETCH_HEAD
```

**Create the pull request**

In case you do not have the push rights in order to merge your changes to the remote repository you need to create Pull Request at the git site, so the owner can pull your changes.

* [Create a pull request](#https://git-scm.com/docs/git-request-pull)

### Get Information About git Files (git ls-files)

* <https://git-scm.com/docs/git-ls-files>

```sh
# Show information about files in the index and the working tree
git ls-files
# Check if file is tracked by git.
git ls-files --error-unmatch FILENAME
```

For example, I got this error:
```
git fatal: no submodule mapping found in .gitmodules for path
```
I used this command to get staged files that git considers to be submodules (160000).
```sh
git ls-files --stage | grep 160000
```
* <https://stackoverflow.com/a/4185579>

### Clean the Working Tree (git stash)

Save the changes from the last commit on and clean them

So the working directory is at the stage of last commit.

```sh
# Saves all differences from last commit away and clean them off (equivalent to git stash push).
git stash

# Shows list of stashes.
git stash list

# Restored changes from the last stash.
git stash apply

# See the most recent stash (equivalent to git stash show -p stash@{0}).
git stash show -p

# See older stash
git stash show -p stash@{1}

# Drop the last stash.
git stash drop
```

### Reset the Current Branch (HEAD) to Specific State (commit) (git reset)

**Undo stuff before commit, i.e. reset the Index and Working Tree or the Index only.**

```sh
# Removes unwanted staging of many files - resets the index only.
git reset

# Deletes all changes from the last commit - resets index and the working tree.
git reset --hard
```

**Remove changes after commit i.e. reset to the specific commit.**

```
# Resets branch (HEAD) to given commit, but the working tree and index stay the same.
git reset --soft HASH_OF_COMMIT

# Resets branch (HEAD) and index to the given commit, files (working tree) stays untouched.
git reset --mixed HASH_OF_COMMIT

# Resets the index and the working tree, everything is reseted to the given commit.
git reset --hard HASH_OF_COMMIT
```

* [git-reset (git-scm.com)](#https://git-scm.com/docs/git-reset)

### Remove (Revert) Changes After Push (git reset, git push, git revert)

**Remove changes and keep history**

```sh
# Revert some existing commits (Requires no local modifications from the HEAD commit)
git revert
```

**Remove changes without history**

```sh
# Move HEAD to the second latest commit
git reset HEAD^

# Do the modifications
# Commit the changes

# Forcefully push the changes (to rewrite the history)
git push -f
```

## Common Scenarios

### Duplicate a Repository

```sh
git clone --bare https://githost.org/OLD_REPOSITORY.git

cd OLD_REPOSITORY

git push --mirror https://github.com/NEW_REPOSITORY.git
```

* [Duplicating a repository (docs.github.com)](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/duplicating-a-repository)

### Move Repository form One Git Site to Another

```sh
# Clone the repository from the old site.
git clone git@GITSITE_OLD.com:USER/PROJECT.git

# Go to the repo directory.
cd PROJECT

# Rename remote origin to old-origin
git remote rename origin old-origin

# Add new remote and call it origin
git remote add origin git@GITSITE_NEW.com:USER/PROJECT.git

# Push everything to the new origin
git push -u origin --all
git push -u origin --tags
```

### Change File (history) in Every Commit

```
# Delete file from every commit
git filter-branch --index-filter 'git rm --cached --ignore-unmatch path/to/file' HEAD

# Move (rename) file through all history
git filter-branch -f --tree-filter 'if [ -d path/to/dir ]; then mkdir -p path/to/new/dir && git mv path/to/dir path/to/new/dir; fi' HEAD
```

* [git filter-branch (git-scm.com)](https://git-scm.com/docs/git-filter-branch)
* [Is it possible to move/rename files in Git and maintain their history?](https://stackoverflow.com/questions/2314652/is-it-possible-to-move-rename-files-in-git-and-maintain-their-history)

## Contribute to a Project

### Contribute to Someone's Repository (with push rights)

```sh
# Clone the repository
git clone git@GITSITE.com:PROJECT_PATH.git
```

**Update the Content from Remote**

If there is a time lag between cloning and the time you want to work on the repository, the remote repository may have changed.
Then it is reasonable to update the local content from the remote i.e. pull the changes.

```sh
git checkout main
# Git pull fetches the last version from the origin (GITSITE:repo) and merges it with the local content
git pull # git pull origin
```

**Develop the Code as a New Branch**

Instead of modifying the main, and pushing to the origin/main.
Create a development branch and make the changes there.
Don't merge the branch with main.
Push the development branch to remote and create a pull request.

```bash
# Create your development branch
git branch BRANCH_NAME

# Check out the branch
git checkout BRANCH_NAME

# Record the changes to be commited
git add PATH_TO_FILE, PATH_TO_FILE_1

# Check if everything is git added or git deleted
git status

# Commit the changes
git commit -m "Meaningful description of the changes"

# Push the local changes to the branch BRANCH_NAME of remote site
git push -u origin BRANCH_NAME
```

### Contribute Without the Rights to Push (fork)

Fork the repository. Clone it and treat it as your own.

Once you are happy with your changes, create a pull request on the GITSITE.

## Submodules

[How To: Merge a Git submodule into its main repository](https://medium.com/walkme-engineering/how-to-merge-a-git-submodule-into-its-main-repository-d83a215a319c)

```sh
# Add submodule
git submodule add https://github.com/NEW_REPOSITORY.git REPO_NAME
```

## Customizing Git

```sh
# List all git configurations with specified origin
git config --list --show-origin
```

### Git Editor and Diff Tool

```sh
# Set vim as your default git editor.
git config --global core.editor "vim"
```

* [How do I make Git use the editor of my choice for commits? (stackoverflow)](https://stackoverflow.com/questions/2596805/how-do-i-make-git-use-the-editor-of-my-choice-for-commits)

```sh
# Set vimdiff as your difftool
git config --global diff.tool vimdiff

# Diff changes with a diff tool of your choice
git difftool
```

* [Configure Git To Use Vimdiff (programster.org)](https://blog.programster.org/configure-git-to-use-vimdiff)

## To Do

* [A simple terminal UI for git commands](https://github.com/jesseduffield/lazygit)
* [How To: Merge a Git submodule into its main repository](https://medium.com/walkme-engineering/how-to-merge-a-git-submodule-into-its-main-repository-d83a215a319c)
* [7.11 Git Tools - Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules)
* [Splitting a subfolder out into a new repository](https://docs.github.com/en/github/using-git/splitting-a-subfolder-out-into-a-new-repository)
* [How to split and merge multiple git repositories while keeping the history](https://dev.to/itminds/how-to-split-and-merge-multiple-git-repositories-and-keep-the-history-2938)
* [Merging Two Git Repositories Into One Repository Without Losing File History](https://saintgimp.org/2013/01/22/merging-two-git-repositories-into-one-repository-without-losing-file-history/)
* [Undo git filter-branch](https://stackoverflow.com/questions/14542326/undo-git-filter-branch)
* https://git-scm.com/docs/git-ls-tree
* [Learn the workings of Git, not just the commands (IBM)](https://developer.ibm.com/tutorials/d-learn-workings-git/)
* <https://git-scm.com/book/en/v2/Git-Basics-Tagging>
