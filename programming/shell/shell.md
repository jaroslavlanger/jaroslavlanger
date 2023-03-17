# Shell 

Command line interface you become addicted to.

`2021 Apr 11, Jaroslav Langer`

## To Do

- [Displey cursore under the prompt](https://unix.stackexchange.com/questions/275684/how-do-i-automate-to-display-cursor-under-the-prompt-on-shell)
- `ls | xargs -I {} echo {}`

## Introduction

This document is written in purpose to simplify the access to the advanced usage of a computer. It started as a notes of a Shell Programming course at UCT, Prague.

**Conventions and symbols**

| Symbols                 | Meaning                                                                                          |
| ---                     | ---                                                                                              |
| `[ ]` (square brackets) | Means optionality i.e. the things inside may be left out.                                        |
| `/` (slash)             | Means exclusive or i.e. it is possible to use either the left or the right part but not both.    |
| `|` (vertical bar)      | Means logical (inclusive) or between the the things on the right and on the left.                |
| `CAPITAL_LETTER`        | Words written in uppercase means they should be substituted - in this case with "A" for example. |

## Basics - shell, terminal, commands

**Difference between shell, terminal, bash, command line and prompt**

- <ctrl><alt><t> opens **terminal emulator** (the window is the terminal emulator).
- The terminal runs the **shell programming language** (bash, dash, zsh or other shell language).
- The line where you can write commands is called the **command line**.
- First letters of the command line that are static (does not change by typing) are called the **prompt**.

* [If not clear see this video](https://www.youtube.com/watch?v=hMSByvFHOro)

**Open terminal**

Press <ctrl><alt><t>.

If it does not work:

1) Open menu ~ press super key (windows key).
2) Type "term" and you should see either "Terminal", "xterm" or something similar.
3) Open it ~ press Enter (double-click).

**Putty access from Windows**

TBD

147.251.253.55

**The terminal enviroment**

Once the terminal is open, what you see is the Command-line interface (CLI). On the left to the cursor is the prompt, which prompts you to take action.

Usually the prompts tells a name of a current user, the name of the machine (hostname) and the location where the user is relatively to the machine (path). Typicaly it also shows, whether the logged user is a normal user ($) or superuser (#).

Example of common appearance could be:

```
USER_NAME@HOSTNAME:PATH$
```

### Shell principle - commands and keywords

Shell is a scripting language, so you can do basically anything as in any other programming language. However shell is also a command language so most of the time you will run commands that someone already made for you. Once you will be able to use these commands, you will probably combine them into shell scripts.

**What happens when I type something to the terminal**

Many words have special meaning. Some words are reserved for the shell programming language, they are called **keywords**, multiple words are **built-in commands** and usually there are also many **executable commands** prepared for you.

### Comments - tell shell to ignore it

Everything between a hash sign `#` and the end of the line is ignored. So it is perfect for making comments or remarks.

```sh
# anything written here is ignored
```

Sometimes I will use the `#` sign to show you the command's output. It is ignored, so it does not matter if you copy-past the lines with it or not.

**command exit**

`exit` command terminates current shell. If you run only one shell, it also close the terminal. Shell is case-sensitive, so while `exit` followed by enter closes the terminal, `Exit` only tells you that `Exit: command not found`.

```sh
Exit
# Exit: command not found
```

**command echo**

Let's start with printing "Hello world!". Type `echo Hello world!` and press enter.

```sh
echo Hello world! # Hello world!
```

### Command Arguments and Options

You can pass arguments to the commands such you passed `Hello world!` to `echo` command. Commonly, the commands also have multiple options to be run with.

Probably the most common option is the option `--help` or `-h` that should help you with the command usage.

```sh
exit --help
# exit: exit [n]
#     Exit the shell.
#     
#     Exits the shell with a status of N.  If N is omitted, the exit status
#     is that of the last command executed.
```

It is common there are two types of options.

* Single letter, starts with hyphen-minus character `-x`
* full text (no spaces), stars with double minus `--xxxx`

So the command structure look like this `command [-o | --options] [arguments]`.

### USE TAB AUTOCOMPLETION

Whenever, you press tab, the terminal autocomplete the word you are writing. If there is more than one posibility, nothing happens. Until you press tab twice.  Than it shows you the all the possible completions.

**It's unbelievable great feature**.

### USE SHELL HISTORY

It is a huge mistake to write commands more than once. Shell remembers what commands you have written, so you can just call them from the history. In case you used it as the previous command, press `[arrow up]`. In case you wrote it some commands ago, press `[ctrl-r]` and start typing, if the result is not what you want, you either press `[ctrl-r]` again for next match, or `[ecs]` to end the search.

* [Search for a previous command with the prefix I just typed (unix.stackexchange.com)](https://unix.stackexchange.com/questions/231605/search-for-a-previous-command-with-the-prefix-i-just-typed)

### Command Types

There are several command types:

| Type       | Description                   |
| ---        | ---                           |
| unknown    |                               |
| builtin    | use `enable` or `compgen -b`  |
| executable | files in `/bin` or `/usr/bin` |
| functions  | defined functions (by user)   |
| aliases    | concatenating more commands   |


**command type**

Let's check the type of the `echo` command.

```sh
type echo # echo is a shell builtin
```

Ok, `echo` is a built-in command. Can i find where it is?

```sh
# type command with option -a
type -a echo
# echo is a shell builtin
# echo is /bin/echo
```

**command enable, command compgen, command function, command alias, command unalias**

```sh
# To enable or disable shell builtins
enable
# List builtins
compgen -b

# Define function
function greet() { echo "hello"; }

# Create alias
alias my_alias='command_1; command_2'
# Destory alias
unalias
```

### More information about commands

**command help, command info, command man, command apropos**

```
man -k
```

### Expansions and suppressions

Not everything you write to shell is interpreted as you wrote it. Some characters are suppressed and others are expanded.

White space characters are suppressed.

```sh
echo   The   triple   spaces   are   shrinken   .
# The triple spaces are shrinken .
```

Some character such as tilda `~` are expanded.

```sh
echo ~
# /home/YOUR_USERNAME
```

There are various [expansions](https://www.gnu.org/software/bash/manual/html_node/Shell-Expansions.html) for now it is good to know this:

**"double quotes"** - prevents all suppressions and expansions except $ notations.

```
echo "~   $USER    ."
# ~   YOUR_USERNAME    .
```

**'single quotes'** - takes it as it is.

```
echo '~   $USER    .'
# ~   $USER    .
```

## Files and directories

### Paths

There is always a need to specify a path to the file a directory you want to work with.
The file can be a document you want to read, an image or simply anything.
Directory is a container for such a files and other directories.
Besides the files and directories the path may specify a command to be used.

There is already a [directory structure](#linux-directory-structure) by default.
Important is that there is one root directory, where every other directories are either in the root directory or nested into its subdirectories. Also every user has its own user directory.
At every point in a terminal you are in some directory.

Directory separator `/`.

```sh
# Show path to the current directory
pwd
# Go (move) to the specified directory
cd /home/username/path/to/the/directory

cd / # go to the root directory
cd . # go to the current directory
cd ~ # go to your home directory
```

If i would have a directory called "tutorial" in my user directory, the path would be

```sh
# The path to the tutorial directory
/home/USER_NAME/tutorial

# or
~/tutorial

# or, if I am in my user directory
./tutorial
```

### Manipulation with files and directories

```sh
# Create new directory
mkdir NEW_DIRECTORY
mkdir -p ./path/to/end/dir # create every dir that does not exist on the path

# Copy files and directories
cp file1 file2  # Copy file1 to file2
cp -r dir1 dir2 # Copy all from dir1 to dir2

# Move file to another place
mv /old/path/to/file1 /new/path/to/file1
# Rename file1 as file2 and check if not overwriting
mv -i file1 file2
# Create new directory and put everything in
mv ./!(dir1) ./dir1/

# Rename directories tutorial_01,tutorial_02,tutorial_03 to t_01, t_02, t_03
for var in 0{1,2,3}; do mv tutorial_$var t_$var; done
# Replace space with underscore
for file in *; do mv "$file" `echo $file | tr ' ' '_'` ; done
# Add word before extension (file_whatever.png -> file_whatever_historical.png)
for file in *; do mv "$file" $(echo ${file%%.*}_historical.png); done

# Delete files and directories
rm file # Remove file
rm -r   # Remove directory (recursively with all files)
```

* [replace spaces link](https://vitux.com/how-to-replace-spaces-in-filenames-with-underscores-on-the-linux-shell/)

### Information about files, directories

**Commands: ls, tree, du, wc, stat**

```sh
# Shows all files of given directory
ls ./path/to/the/directory

# Show structure of all files and dictionaries from your dictionary 
tree

# Shows counts of lines, words and bytes
wc FILE_NAME
# show number of lines (-l) words (-w) and bytes (-c)
wc -l FILE_NAME

# Recursively shows sizes (disk usage) of directories and files 
du ./path/to/the/directory 
# Show size of the DIRECTORY and its direct children (2 ~ levels down etc.) 
du -d 1 ./path/to/the/DIRECTORY
# Display info in human readable form (-h) only for the top folder (-s)
du -hs FILE_NAME
# Display all file and directory sizes
du -a

# show file statistics
stat file1
```

### Compression and decompression

(Uploading and downloading in ohter way is **damn** slow)

**Command zip**

Zip files into new.zip

```sh
zip new file1 file2 file3
```

Unzip files from new.zip

```sh
unzip new.zip
# to NEW_DIR
unzip new.zip -d PATH/NEW_DIR
```

**Command tar**

Compress files to new.tar.gz

```sh
# -c = create
# -v = verbose
# -z = gzip / gz / zip
# -f = following files

tar -cvzf new.tar.gz file1 file2 file3
```

Decompress from new.tar.gz

```
# -x = extract

tar -xvzf oldFile.tar.gz
```
Decompress from new.tar.bz2

```
# -j = bz2
# -C = where to extract

tar -xvjf oldFile.tar.bz2 -C /path/Directory
```

* [How to use Tar Command in Linux with examples (interserver.net)](https://www.interserver.net/tips/kb/use-tar-command-linux-examples/) |
* [How to Extract (Unzip) Tar Bz2 File (linuxize.com)](https://linuxize.com/post/how-to-extract-unzip-tar-bz2-file/)

### Links

**soft link**

Points to the original file, can be used as the original file for multiple purposes.

```sh
# Ways to create soft links
ln -s FILENAME LINKNAME
cp -s FILENAME LINKNAME
```

Example Usage
* I installed "code_like_hell" editor with the executable file at /usr/share/code_like_hell/bin/code_like_hell
* I want to open the editor just by typing `ch` to the terminal.
* So I create an symbolic link called `ch` at the `/usr/bin` directory.

```sh
ln -s /usr/share/code_like_hell/bin/code_like_hell /usr/bin/ch
```

**hard link**

Acts like a synchronized copy of the original file, change in one file changes the other.

```sh
# Hard link creations
ln FILENAME LINKNAME
cp -l FILENAME LINKNAME
```

### Globbing and Wildcards

Glob patterns specify sets of filenames with wildcard characters. Wildcards are symbols with special meaning. It is especially useful when we don't know the exact name or if we perhaps want to use more than one name to do something.

```sh
# Question Mark
? # Matches one character within one directory.

# Single Asterisk
* # Matches zero or more characters within one directory.

## Double Asterisk
** # Matches matches zero or more characters across multiple directories.

# Square Brackets Range
[a-dsu] # Matches one character from the range i.e. a,b,c,d,s,u
[3-7a-g]

# Square Brackets Group
[:digit:] # Equals to [0-9]
[:alpha:] # Equals to [a-zA-Z]
[:alnum:] # Equals to [0-9a-zA-Z]
[:upper:] # Equals to [A-Z]
[:lower:] # Equals to [a-z]

# Not containing anything from bracket
[!a] # Matches one character that is not letter a. Equivalent of [^ ] in RegEx.

# Examples
ls ?[[:digit:]]*
ls ?[4-6]
```

* [More information](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/x11655.htm)
* [What do double-asterisk wildcards mean?](https://stackoverflow.com/questions/28176590/what-do-double-asterisk-wildcards-mean)

### Find anything

#### locate

```sh
locate -b -i -n 17 -S -u
```

#### find

```sh
find /  -name   "toBeFound"     ACTIONS -delete
        -regex  '.*anything.*'
        -type f d l s                   -ls 
        -user                           -exec ls -l {} \;
        -size   +-nc k M G              -ok
        -empty
        -mindepth -maxdepth n
        -perm 	400 	u=rw 	-u=rmw 	/u=r,o=x
		-user 	langera
		-group
```

### Read files

```sh
# Create new (empty) file
touch path/to/my/newFileName.anything

# Output every line from file
cat file

# Output every line from file in reverse order
tac file

# Output first 5 lines from file in reverse order
head file
# Output first n lines from file in reverse order
head -n 3 file

# Output last 5 lines from file in reverse order
tail file
# Monitor a file as that other software writes to
tail -f
```

### Standard input, standard output, standard error output (Stdin, stdout, stderr)

```bash
# 0<      1> >>   2>       
# 1> where_to     2>&1
# &> where_to

# Take output of command and writes it to the file
# COMMAND > FILE
echo Hello world! > file_example.txt

# Take output of command and writes it at the end of file
# COMMAND >> APPENDED_FILE
echo Hello another world! >> file_example.txt
```

* [what-are-stdin-stdout-and-stderr-on-linux](https://www.howtogeek.com/435903/what-are-stdin-stdout-and-stderr-on-linux)

### Pipe - command output redirection

Connects standard output of one command to the standard input of another command.

```bash
# any_command | sort, uniq, less, head
# tee
# file

# Sort output
sudo du -a | sort -n -r | head -n 20
```

Named pipes (Advanced)

```sh
mkfifo pipe2
ls > pipe2
cat < pipe2
```

* [mkfifo (how to forge)](https://www.howtoforge.com/linux-mkfifo-command/)

### Compare two files

**Command diff**

```
# Show differences of files FILE_A, FILE_B (e.g. "< UNIQUE LINE OF FILE_A")
diff FILE_A FILE_B

# Unified format - more information about the files, changes have a context
diff -u FILE_A FILE_B

# Compare file with a pipe redirection
SOME_COMMAND | diff FILE_A -

# Show non-printing characters
diff FILE_A FILE_B | cat -t
```

* [Linux diff command (computerhope)](https://www.computerhope.com/unix/udiff.htm)
* [How to compare two files for non-printing characters (superuser.com)](https://superuser.com/questions/560050/how-to-compare-two-files-for-non-printing-characters)


Show differences side by side (usually preferred, not always)

```sh
# Show differences side by side
diff --side-by-side --suppress-common-lines FILE_A FILE_B

# See the difference line by line with more command
diff -y --suppress-common-lines FILE_A FILE_B | more

# Get number of different lines
diff -y --suppress-common-lines FILE_A FILE_B | wc -l
```

* [How can i make "Diff" only show differences between two files? (community.spiceworks.com)](https://community.spiceworks.com/topic/85704-how-can-i-make-diff-only-show-differences-between-two-files) |

**Command cmp**

```sh
cmp file1 file2
```


## Install stuff

### Install from official repositories

```sh
sudo apt-get install ALMOST_ANYTHING
```

### Install from package .deb

Works the same way for an update.

```sh
sudo dpkg -i PACKAGE_NAME.deb
# attempt to fix corrupted dependencies
sudo apt-get install -f
```

* [source](https://unix.stackexchange.com/questions/159094/how-to-install-a-deb-file-by-dpkg-i-or-by-apt)

### Version of installed software

```sh
# Most of the programs have implemented option --version
COMMAND_NAME --version
```

### Search for package

```sh
apt-cache search KEYWORD
```
[source](https://askubuntu.com/questions/160897/how-do-i-search-for-available-packages-from-the-command-line)

### Check if installed

```sh
dpkg-query -l 'someth'
```

## User management and privileges

### TBD Basic commands

```sh
groupmod
whoami
who
groups
```

### Add,delete  user | group

```sh
adduser USERNAME
deluser USERNAME
groupadd GROUPNAME
goupdel GROUPNAME
```

### Add user to group

```sh
usermod -a -G GROUP USER
```

### Group information

Read file containing information about groups.
Every line of the file has following structure:
GROUP_NAME:PASSWORD:GROUP_ID:GROUP_USER_1, GROUP_USER_2, GROUP_USER_3

```sh
less /etc/group
```

### Change password

```sh
[sudo] passwd [username]
```

### Switch user

```sh
su USERNAME
```

Every su opens a new shell.

```sh
# Show number of open shells
echo $SHLVL
```

### Superuser

Login as superuser, superuser password required.
```sh
su
```
Login as superuser, current user's password required.
```sh
sudo su
```
Grant to the command privileges of superuser.
```sh
sudo COMMAND
```

### User permissions

Everything has permissions set.

Example

```sh
ls -la
#drwxrwxrwx NUMBER USER USER NUMBER DATE NAME_OF_THE_FILE
```
The first 10 letters are the permissions, the structure follows
```
-        ---  ---   ---
filemode user group others
```

File types

+ d - directory 
+ l - link 	
+ b - bloc type (harddisc) 
+ c - chartype

### Change permissions

```
chmod u-x
	rename needs directory privileges
	to read files directory needs r+x
	to rename files directory needs w+x
	--- 000	0
	--x 001 1
	-w- 010 2
	-wx 011 3
	r-- 100 4... 	chmod 755 text.txt chmod u=rw,g+rw ccc.txt
```

```sh
/etc/shadow

setuid bit 		chmod 	u+s ... 4777
setgid bit 		chmod	g+s ...	2777
sticky bit 		chmod	+t ...	1777

umask	0224		d- 777	f- 666
```

### Change ownership

```sh
chown USER[:GROUP] OBJECT
```

## Useful commands

### Get basic info about command

```sh
# Path to the executable file i.e. command COMMAND
which COMMAND

# One line information
whatis COMMAND
# Equivalent to
man -f COMMAND
```

### Show big files in a terminal

```sh
# Output stays into terminal after pressing q to quit
more
# File open in vim-like environment after pressing :q to quit the terminal is clean
less
```

### Open anything in terminal

Works like double-click
```sh
xdg-open ANY_NAME.ANYTHING
```

### split

- Split content

```bash
# Split file into multiple n-lines files
split -l 100 FILE_NAME NEW_NAME
# Split file into 50MB files, with numerical suffix
split -d -b 50m data.csv data_ --additional-suffix='.csv'
# Proportionally split file into n files
split -n 3 filename a
# Change suffix length (by default 2 characters)
split -n 3 -a 5 filename
```

### cat

- Concatenate content

```bash
cat file_0* > merge                              # merges all the files named file_01 file_02 etc.
echo "First line" | cat - second_file            # minus make the first file_stream from stdin
echo "first" | cat - lines > tmp && mv tmp lines # prepend "first" to lines file.
```

* [prepend text to file](https://www.cyberciti.biz/faq/bash-prepend-text-lines-to-file/)

### cut

- Extract sections from each line of files

```bash
# Get the Nth column (numbered from 1), implicit separator is `tab`
cut -f 3 filename   # get third column
cut -f 1,3 filename # enumerated columns
cut -f 2-3 filename # range of columns

cut -d ':' -f 1 /etc/password | head # define separator

cut -c 2-10 # extract characters (one character one column)
```

### paste

- merge columns/rows

```bash
paste file1 file2 file3         #(implicitni oddelovac je TAB)
paste -d ':' file1 file2 file3  #(explicitni definice oddelovace)
paste -s file1 file2 file3      #(spoji obsahy jednotlivych souboru za sebou po radcich)
```

### sort

```bash
# Sort and merge multiple files
sort file1 file2 file3 > file
cut -d ':' -f 1 /etc/passwd | sort

sort -r file # sort in reverse order

sort -n file # Numeric sort not lexicographic

cut -d ':' -f 3 /etc/passwd | sort
cut -d ':' -f 3 /etc/passwd | sort -n

sort -k file # sort by k-th columns (separator is `tab` by default)

# (seradi numericky podle klice = od 5. sloupce v tabulce)
ls -l | sort -nr -k 5

# (razeni podle vice klicu)
sort --key=1,1 --key=2n filename

# (offset v ramci sloupce)
sort -k 3.7nbr -k 3.1nbr -k 3.4nbr filename

# (explicitni definice oddelovace)
sort -t ':' -k 7 /etc/passwd
```

### shuf

```bash
# Get random N lines from input
shuf -n N input > output
```

### wget - download file from url (webpage, image, etc.)

```sh
wget https://static.boredpanda.com/blog/wp-content/uuuploads/cute-baby-animals/cute-baby-animals-2.jpg
```

### Browser folders like a pro

Ranger

```sh
sudo apt-get instal ranger # install ranger
ranger # start ranger
```

| key   | action                                |
| ---   | ---                                   |
| j k   | move up, move down                    |
| h l   | move level up, move into directory    |
| s     | open terminal console                 |
| zh    | see hidden files and directories      |
| / n N | search, go to next, previous match    |

* [ranger (digitalocean)](https://www.digitalocean.com/community/tutorials/installing-and-using-ranger-a-terminal-file-manager-on-a-ubuntu-vps)

### show terminal height and width

```sh
# show height
tput lines
# show width
tput cols
```

### Push process the background

"I have opened something with terminal, now i see the process and can not use the terminal anymore"

Situation as described is the single most common example when is super nice to push the process to the background.

**How to do it?**

Press **Ctrl+Z**, then type

```sh
bg
```

The proccess will continue in background.

If you want to bring the process back to the foreground, type

```sh
fg
```

* [How to run programs from a linux terminal without blocking the terminal? (superuser.com)](https://superuser.com/questions/154486/how-to-run-programs-from-a-linux-terminal-without-blocking-the-terminal)

### Copy from terminal to clipboard

```sh
pwd | xclip -selection clipboard
```

* [copy to clipboard current path from console with no mouse \[duplicate\] (askubuntu.com)](https://askubuntu.com/questions/597788/copy-to-clipboard-current-path-from-console-with-no-mouse)

### calculator bc

```sh
echo "scale=2; 3/2" | bc

echo "obase=10; ibase=2; 1101" | bc
```

### Get Date

```sh
date            # Get current date
date -r FILE    # Get last modification date of a file
date +%T.%N     # Specify the datetime format (start with + for datetime format use %)
```

### See images in asciiart

```sh
cacaview image.jpg
```

## SSH

```sh
ssh USER@99.888.777.22
```

### Copy files over ssh

scp [OPTION] [user@]SRC_HOST:]file1 [user@]DEST_HOST:]file2

```sh
scp -r compute  USER@78.128.250.10:/home/USER/computing/
```

[scp link](https://linuxize.com/post/how-to-use-scp-command-to-securely-transfer-files/)

### Screen

```sh
# How to use screen from terminal
screen      # Create screen 
screen -d   # Detach from screen
screen -r   # Reattach to screen
screen -ls  # List all screens

# Kill screen
screen -X -S SESSION_ID_FROM_LS kill
```

* [screen link](https://linuxize.com/post/how-to-use-linux-screen/)
* [kill screen](https://stackoverflow.com/questions/1509677/kill-detached-screen-session)

**How to work inside of a screen**

Press `Ctrl+a+OPTION`

| OPTION | Action             |
| --- | ---                   |
| c   | create new bash       |
| "   | show open bash        |
| S   | devide horizontaly    |
| |   | devide verticaly      |
| tab | change region         |
| A   | rename region         |
| k   | kill actual screen    |
| X   | close region          |
| Q   | close regions         |
| esc | relase cursor up/down |

### SSHFS

### Mount local direcotry to remote directory

```sh
sshfs $USER@remote.example.com:/home/$USER/code ~/remote_code
```
### If user on local is different than the one logging with ssh

Uncomment user allow_other in /etc/fuse.conf

```/etc/fuse.conf
user_allow_other
```

```sh
sshfs -o allow_other user@myserver:/home/user/myprojects ~/mount/myprojects
```

### Unmount

```sh
fusermount -u ~/mount/myprojects
```

## Processes

```sh
# shows processes
top
```

### Find process

```sh
ps aux | grep cat
```

### Kill process

```sh
# kill one specific precess id
kill -9 3827

# kill family of proceses
killall -9 chrome
```

* [source](https://www.linux.com/training-tutorials/how-kill-process-command-line/)

## Environments and variables

Variables and functions, can be exported (global) or not.

### set

can be used to set various shell options, or the positional parameters. If no arguments or options are given, then it prints all shell variables and functions.

### Print value of variable

```sh
echo ${...}
```

### compgen -v

Outputs only names of all shell variables, exported or not.

* [compgen](https://askubuntu.com/questions/953579/what-is-the-difference-between-env-declare-and-compgen-v)


### GLOBAL: env, printenv ...

```sh
# Export can be used to export variables or functions.
export
# With the -p option, it prints exported variables and functions
export -p
```

**env**

The env command can run other commands with modified environments. If no command is given, env prints environment variables (i.e., exported variables).

### printenv

Prints environment variables.

### LOCAL

```
set | grep ''
var_a=123a
```

```sh
# CONSTANTS
$USER; $PATH; $SHLVL; $SHELL;

# variables
name=value [[:alnum:]]

unset ... (local)
declare [-i; -r] ...
```

### Open new shell

```sh
# Open (some) shell
bash # open bash
dash # open dash
sh   # open shell

# Tell current shell language
echo $0
# See shell level
echo $SHLVL
# exit shell i.e. go to the previous enviroment
exit
```

```sh
bash    child[sub]   interactive / uninteractiv - | read   
```
```sh
startup
```

```sh
login shell            
    /etc/profile
    $HOME/ [.profile; .bash_profile; .bash_login]
non-login shell
    /etc/.bashrc
    $HOME/.bashrc
    source
```

### History

settings of history file 
```sh
~/.bashrc
```
Edit size of history command and history file
```sh
HISTSIZE=1000
HISTFILESIZE=10000
```
path to historyfile
```sh
echo $HISTFILE
```
how to stop logging ls command in history
```sh
echo 'export HISTIGNORE="ls:tree:cat:tail:head:bash"' >> ~/.bashrc
```
run 111st command
```sh
history !111
```

press - ctrl+R - for searching of a commands from past

[Source](https://www.rootusers.com/17-bash-history-command-examples-in-linux/)

## Text transformation

### tr

```sh
# Example: Remove spaces from filename
ls # name\ with\ spaces.txt
for file in *; do mv "$file" `echo $file | tr ' ' '_'` ; done
ls # name_with_spaces.txt
```

Translate, squeeze, and/or delete characters from standard input, writing to standard output.

```
tr [OPTIONS] SET1 [SET2]
```

Translate charactes

Command expects arguments `SET1 SET2` where SET1 are characters to be translated with SET2.
prikaz ocekava dva argumenty: sadu znaku, ktere ma nahradit a sadu znaku, kterymi je ma nahradit
sady znaku mohou byt vyjadreny tremi zpusoby

```sh
# Characters specified by enumeration
echo "characters" | tr abc 123
# Characters specified by range
echo "characters" | tr a-z 1-3
echo "chArACtERs" | tr a-z A-Z
# Characters specified by POSIX
echo "chArACtERs" | tr [:lower:] [:upper:]
# First range is shorter - nothing special
echo "aaabbbccc" | tr a-b 1-3
# First range is longer - characters from SET1 without partner are replaced with last form SET2
echo "aaabbbccc" | tr a-c 1-2
```

Remove characters

```sh
# remove characters
echo "aaabbbccc" | tr -d ab
# replace repetitions with one occurance
echo "aaabbbccc" | tr -s ab 
echo "abcabcabc" | tr -s ab
```

## Expansions

```sh 
# wild cards * ? ' ' $
mv old/* new/

# paths \ . ..
ls ..

# brace expansion {}
mkdir task_{a,b,c} # mkdir task_a task_b task_c
mkdir task{01..03} # mkdir task01 task02 task03

# tilde expansion
ls ~/Documents # ls /home/$USER/Documents

# parameter and variable expansion
variable=10
echo ${variable} # echo 10

# command substitution
echo Hello \"$(ls)\" folders!

# arithmetic expansion + - * / % ** ++ --
echo $((1238 % 17)) echo 14

# word splitting
# filename expansion
# quote removal
```

* [Documentation](https://www.gnu.org/software/bash/manual/html_node/Shell-Expansions.html)

## Regular Expressions

`“REGEX” or “REGEXP”?  ->  /REGEXP?/`

**BRE ERE**

- BRE = Basic Regular Expressions
  - `. * [^- ] ^ $`
- ERE = Extended Regular Expressions
  - `+ ? { } ( ) | \`

**Classes**

- Enumerated classes: `[abc987]`
- Range-based classes: `[a-e5-8]`
- POSIX classes `[: :]`

| POSIX       | Classes       |
| ---         | ---           |
| `[:alpha:]` | `[a-zA-Z]`    |
| `[:digit:]` | `[0-9]`       |
| `[:lower:]` |               |
| `[:upper:]` |               |
| `[:alnum:]` |               |
| `[:word:]`  | `[a-zA-Z_]`   |
| `[:blank:]` | `[\ \t]`      |
| `[:xdigit]` | `[a-fA-F0-9]` |

**Quantifiers**

| Quantifier   | Description                              |
| ---          | ---                                      |
| `*`          | Any quantity                             |
| `+`          | At least once                            |
| `?`          | Once at maximum                          |
| `{min, max}` | within min, max range includeing min max |

**Special characters**

| s.c. | Desc. |
| ---  | ---   |
| \b   |       | 
| \<   |       | 
| \>   |       | 
| \w   |       | 
| \W   |       | 
| \s   |       | skoro_i
| \d   |       |

**Alternations**

`RE1|RE2`

**Groups**

`'<(h[1-6])>.*</\1>'`

Commands

```bash
# BRE
grep - BRE

# ERE
egrep
grep -E
grep \ERE 
```

### Grep

Usage: `grep -options 'RE' where`

options: `-n -c -i -v`

- fgrep
- rgrep

Examples

```bash
less /
locate --regexp [bre] --regex [ere]
```

## Move in terminal

- alt B / F

### Manipulation with text in terminal

- alt U / l
- alt t
- ctrl t
- kill ring CTRL K ctrl+y alt y

## sed

- stream editor pro filtrovani a transformaci textu


Usage: `sed options 'script' file`


**options**

```
-n  potlaci autoprint radku
-i  potlaci presmerovani na obrazovku a zmeny zapise do souboru
```

**addresses**

```
n           cislo radky
addr1,addr2 rozsah radku
first~step  prvni a kazdy dalsi po definovanem kroku
$           posledni radka
addr1,+n    zacatek a n nasledujicich radku
addr!       vsechny ostatni radky krome definovanych (definovane mohou byt vsemi uvedenymi zpusoby)
/regexp/    radka, ktera splnuje definovany BRE vyraz (delimiter je delimiter / nebo \cregexpc kde c je libovolny znak)
```

**commands (singleline)**

```
p   tisk vybraneho radku
    sed 'p' filename
    sed -n 'p' filename
i   vlozi text pred aktualni radek
    sed 'i text' filename
a   vlozi text za aktualni radek
    sed 'a text' filename
d   vymaze aktualni radek
    sed 'd' filename
    sed '2~2d' filename
=   zobrazi cislo aktualniho radku
    sed '=' filename
    sed '2,5=' filename
c   zmeni text aktualniho radku
    sed '2c text' filename
    sed '2,5c text' filename
r   cteni radku ze souboru
    sed 'r input1' input2
    sed '2,3r input1' input2
w   zapis radku do souboru
    sed 'w input' output    (alternativa k cp)
    sed '2,3w input' output
s/regexp/replacement/   substituce
     echo "pes" | sed 's/pes/kocka/'
    sed s/pes/kocka/ filename > newfilename            
    replacement
        muze obsahovat znak &, ktery vlozi text definovany regularnim vyrazem
        muze obsahovat back references \1 - \9
    flags
        prikazu s mohou nasledovat ruzne priznaky
            echo "aaabbbccc" | sed 's/b/1/'   (nahradi pouze prvni vyskyt)
            echo "aaabbbccc" | sed 's/b/1/g'  (nahradi globalne v celem radku)
            echo "aaabBbccc" | sed 's/b/1/Ig' (nahradi globalne v celem radku a ignoruje velikost pismen)
y/set1/set2/   transliterace
    echo "aaabbbccc" | sed 'y/abc/123/'
         na rozdil od prikazu tr vyzaduje stejnou delku znakovych sad
         nepodporuje rozsah (-) ani POSIX znakove tridy => vycet znaku musi byt presne definovan
```

**Other**

```bash
# vice prikazu najednou (oddeluji se strednikem ve slozenych zavorkach s option -e)
sed -e '{s/pes/slon/; s/oves/zito/}' filename
sed -e 's/pes/slon/; s/oves/zito/' filename
sed 's/pes/slon/; s/oves/zito/' filename
```

```bash
# aplikace transformaci ulozenych v souboru (kazdy prikaz na samostatnem radku)
sed -f script.sed filename
    script.sed
        s/pes/slon/
        s/oves/zito/
```

```bash
sed i a =   p d n
            P D N
#   sed '/prvni/{N; s/\n/ /}' radky2
#   sed '=' radky2 | sed '/[1-9]/{N; s/\n/ /}'
#   sed '/^$/{N; /treti/D}' radky1
```

## Shell scripts

Commands are great, now let's get rid of the command repetitions by writing scripts.

```sh
shell
    max 255 znaků
    echo $0
    PATHS: /etc/shells
    chsh username
script
    exec. - $PATH / path/script 
    #!/bin/bash
    $0
    basename $0
    $1 - $9 ${10} - $#
    
    read -> $REPLY
    options:
        respons respons1 ...
        -n 3 
        -p "zadej cislo: "
        -t secs
        -s
        IFS = ':'
        X NEVER - echo "abc" | read
```

### Call a script

`. (source or dot operator)`

```bash
# .
. path/to/file.sh
# source
source path/to/file.sh

# Add executable right and use the file as command
chmod +x ./path/to/file.sh
# execute
./path/to/file.sh
```

* [. (source or dot operator)](https://ss64.com/bash/source.html#:~:text=source%20is%20a%20synonym%20for,maximum%20compatibility%20use%20the%20period.&text=When%20a%20script%20is%20run%20using%20'source'%20it%20runs%20within,available%20after%20the%20script%20completes.)

#### Call scripts inside of a script

```bash
#!/bin/bash

MY_SCRIPT=/path/to/script.sh

$MY_SCRIPT input_1 input_2
```

* [Why doesn't my Bash script recognize aliases?](https://unix.stackexchange.com/questions/1496/why-doesnt-my-bash-script-recognize-aliases)


### Comments

Comments are also more useful for writing bash scripts but it is important to know what the hesh means.

```bash
<<< #here-string
```

```bash
#<< OPENCLOSE  #here-document 
OPENCLOSE

# same as

#<< _COMMENT_
lalala
_COMMENT_

# Commad True
True '    '
# Same as
:' '
```

### Variables

Define variables

```bash
# var=value - spaces must be escaped
number=1       # number
string=hello # strings

# Arrays
array=(1 2 nn pp gg)    # space separated array
arr[3]=there            # define with index
```

Access variables

```bash
echo ${var}

# Access array
echo ${arr} # first item
echo ${arr[0]} # first item
echo ${arr[1]} # second item

echo ${arr[@]} # full array
echo ${arr[*]} # array as a string
```

Shell parameter expansion

```bash
var=
# :-value -> pokud v proměnné není nic, vypíše se value, ale nepřiřadí se
echo ${var:-nothing}
echo $var
# :=value -> přiřadí i proměnnou(taková default)
echo ${var:="value "}
# :? -> na prázdnost,vrátí -1, nebo zvolenou hlášku
echo ${var:?"value "}
# :+123 -> pokud není prázdná, dočasněji změn na 123
echo ${var:+"value "}
```

```bash
# vrátí podle vzoru všechny proměnné, které mu odpovídají
echo ${!pattern} 
echo ${!S*}
```

```bash
# Make first letter uppercase # lowercase
echo ${var^} # ${var,}
# Make all letters uppercase # lowercase
echo ${var^^} # ${var,,}
#  nahraď pattern valuelem :P -> pouze pro 1. výskyt vzoru
echo ${var/pattern/value}
# Change all pattern matches with value
echo ${var//pattern/value}
# #pattern -> trim pattern form left
${var#pattern}
# ##pattern -> trim longest pattern form left
${var##pattern}
# %pattern    -> trim pattern from right
${var%pattern}
# %%pattern   -> trim the longest pattern from right
${var%%pattern}
```

* [lowercase uppercase strings](https://linuxhint.com/bash_lowercase_uppercase_strings/)
* [Shell Parameter Expansion (gnu.org)](https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html)

```bash
# :offset -> usekne 4 znaky od začátku a pouze do 6
echo ${aaa:4:6}
# : -offset -> od konce
echo ${aaa -6:3}
```

**Cast string to integer**

```sh
num=$(($num+0))
```

* [Bash: comparing a string as an integer (stackoverflow.com)](https://stackoverflow.com/questions/16264311/bash-comparing-a-string-as-an-integer/17093431)

#### Numbers (arithmetic expansion)

```bash
# Operators + - * / % ** ++ --
echo $((10)) # 10
# Octal base
echo $((010)) # 8
# Hexadecimal base
echo $((0x10)) # 16
# Base#Number
echo $((7#13)) # 10
```

* [math in bash scripts](http://faculty.salina.k-state.edu/tim/unix_sg/bash/math.html)

#### Variable Scope

```sh
[implicit (global) | local optional] variablename
```

### Tuples

```sh
OLDIFS=$IFS
IFS=','
for i in c,3 e,5; do
    set -- $i
    echo $1 and $2
done;
IFS=$OLDIFS
```

* [Loop over tuples in bash? (stackoverflow.com)](https://stackoverflow.com/questions/9713104/loop-over-tuples-in-bash)

### Printf

{% raw %}
```bash
printf "{%s: %s}\n" "$m_key" "$m_name"
```
{% endraw %}

### Exit status

Every command in bash returns a status, number between 0 and 255, 0 menas success.

```sh
# Read the last exit status
echo $?
# See exit status of my_script
my_script -opt file_name; echo $?
```

Bash script or terminal itself can return status code, command exit

```sh
# Success
exit # exit 0
# Failure
exit 1 # exit 255

# Commands true and false
true # ignore any input and exit 0
false # ignore any input and exit 1
```

### Bracket tests

#### Square bracket test

Example usage: `[ unary_op argument ]`

**The space after the first and before the second bracket are required** 

Unary test operators

| unary_op | description             |
| ---      | ---                     |
| -f       | is file                 |
| -d       | is directory            |
| -L       | is symbolic link        |
| -r       | is readable by test     |
| -w       | has permision to write  |
| -x       | is executable           |
| -s       | is not empty            |

Example

```bash
[ -s experiment]; echo $?
```

Three arguments usage: `[ arg1 binary_op arg2 ]`

Example
```bash
# is file1 olther than file2
[ file1 -ot file2 ]; echo $?
```

Test strings

| binary_op | description |
| ---       | ---         |
| -n        |             |
| -z        |             |
| =         |             |
| !=        |             |
| <         |             |
| >         |             |

Test numbers

| binary_op | description |
| ---       | ---         |
| -eq       |             |
| -ne       |             |
| -lt       |             |
| -le       |             |
| -gt       |             |
| -ge       |             |

Example:

```bash
n=5
if [ $n -lt 10 ]; then echo n is lower than 10; fi

[ f1 -nt f2 ]; echo $?
```

**Double square bracket test (Bash only)**

Usage `[[_arg1 op arg2_]]`

1) Numbers can be compared straight `x1` (not $x1)
2) `x1 == x2(d)`
3) `x1 =~ ERE`


**Double bracket test**

Usage `((_arg1 op arg2_))`

1) `$x1 .... x1` i pro stringy
2) `==` funguje pro cisla

Assign value

| binary_op | description |
| ---       | ---         |
| `+=`      |             |
| `-=`      |             |
| `/=`      |             |
| `%=`      |             |
| `*=:`     |             |
| `++`      |             |
| `--`      |             |

Ternary operator (conditional)

- `(( arg1? arg2 : arg3 ))`

```
(( a<1? (a=+2) : (a-=3) ))
```

Logic operators

```
AND     -a 		&&
OR      -o 		!!
NOT     !		!
```

### Conditions

```sh
if commands; then commands; fi

if [[ condition ]]; then
	commands
elif [[ condition ]]; then
	commands
else
	commands
fi
```

Usually the `if` statement is not needed.

```
# Usage
command1 OPERATOR command2
```

| OPERATOR  | Action |
| ---       | ---    |
| `;`       | Executes both commands (it is the same as type the enter)             |
| `&&`      | Executes the command2 if the command1 exit code was 0 (AND)           |
| `||`      | Executes the command2 only if the command1 exit code was not 0 (OR)   |
| `&`       | Executes the command2 right after the command1 no matter what         |

```bash
case variable in
pattern)
    commands;
;;
pattern2) commands;
;;
esac
```

PATERN:

```
letter)
*)
?)  e.g.    ???.txt)
[abc])  OR  [3-9])  OR  [[:digit:]])
```

```bash
select variable in[list] do
    commands;
done
```

### Loops

**For loop**

```bash
for  var [in ${LIST}]; do
    commands;
done

# words
for var in a b c; do echo $var; done
for var in a" b c"; do echo $var; done
for var in word1 word2; do echo $var; done

# Files
for var in ~/path/*; do echo $var; done

# Ranges
for var in {3..9}; do echo $var; done
for var in {3..9..3}; do echo $var; done

# Arrays
array=(1 2 3)
for var in ${array[@]}; do echo $var; done

$@  # when missing [in list], uses argument from input
for $@; do

for ((i=0; i<10; i++))
```

* [for loop link](https://www.cyberciti.biz/faq/bash-for-loop/)

**while loop**

```sh
while commands; do
    commands;
done

while IFS=":" read a b c; do echo $a, $b, $c; done < /etc/group

until commands; do
    commands;
done

break number    # breaks to the defined level 
continue number # implicit 1; starts next iteration of def. loop
```

### Arguments

```sh
# Echo arguments (get argument by number)
echo $0 # Argument 0 - how the script was called
echo $1 # First argument
echo $2 # second argument

echo $# # Number of arguments

echo $* # All arguments as one string
echo $@ # Array of all arguments

# shift the arguents number
shift   # shift it by one
shift 4 # shift it by 4
```

* [Process all arguments except the first one in a bash script](https://stackoverflow.com/questions/9057387/process-all-arguments-except-the-first-one-in-a-bash-script)

### Functions

What function can and can not do
- `return` code in range 0-255
- `exit` script with code 0-255
- function has its own positional parameters e.g. $1 $@ (does not change the script one)
- it can change variables that are outside of that function
- anything else as code outside of a function

```sh
function name {
    commands;
}

name () {
    commands;
}

return # if not, then exit status of function is the es of last function
```

Return string from function
```sh
# The key is to echo at the last line of the function
get_str() {
    # Multiple lines of anything
    echo str
}

x=$(get_str)
```

* [More - functions (shellscript)](https://www.shellscript.sh/functions.html)
