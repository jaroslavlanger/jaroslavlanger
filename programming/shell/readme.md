# Shell

## References

* <https://www.gnu.org/software/bash/manual/bash.html>

## Introduction

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

## Call a script

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

### Call scripts inside of a script

```bash
#!/bin/bash

MY_SCRIPT=/path/to/script.sh

$MY_SCRIPT input_1 input_2
```

* [Why doesn't my Bash script recognize aliases?](https://unix.stackexchange.com/questions/1496/why-doesnt-my-bash-script-recognize-aliases)


## Comments

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

## Variables

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

## Numbers (arithmetic expansion)

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

## Variable Scope

```sh
[implicit (global) | local optional] variablename
```

## Tuples

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

## Printf

{% raw %}
```bash
printf "{%s: %s}\n" "$m_key" "$m_name"
```
{% endraw %}

## Exit status

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

## Bracket tests

### Square bracket test

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

## Conditions

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

## Loops

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

## Arguments

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

## Functions

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
