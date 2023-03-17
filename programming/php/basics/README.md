# Absolute Basics of PHP

## MENU

+ [Header PHP tag](#header-php-tag)
+ [Printing](#printing)
+ [Comments](#comments)
+ [Read Input](#read-input)
+ [Variables](#variables)
+ [Data Types Recognition](#data-types-recognition)
+ [Strings](#strings)
+ [Arrays](#arrays)
+ [Conditions](#conditions)
+ [Loops](#loops)
+ [Time Measuring](#time-measuring)
+ [Assertions](#assertions)

## Header PHP tag ##
PHP file must begin with:
```
<?php
```
May also end with
```
?>
```
#### Most save is to have PHP files with only PHP code, whichstarts with tag ```<?php``` and without any closing tags.
---
## Printing
### For text and simple datatypes
```
echo "hello php";
```
### For more complex datatypes
```
var_dump($variable);
```
### Another way
```
print_r($variable);
```
### Concatenating string
```
echo '$var '.$var."\n";
```
---
## Comments
### Single lines
```
// with slashes

# with hash 
```
### Multi-lines
```
/*
comment
*/
```
or with docstring / herestring
```
$doc = <<<SAMEPHRASE
As many lines of text
as you wish to have.
SAMEPHRASE;
```
---
## Read Input
```
$input = file_get_contents($argv[1]);
```
### The $argv is array of arguments. The zero argument is the file itself. You can use it as any array such with end() etc
```
$input = file_get_contents(end($argv));
```
### import code once - error will stop the code.
```
require_once './the/path/you/desire.php';
```
### import code once - only warrning will be shown if error.
```
include_once './the/path/you/desire.php';
```
### Or you can include | require all over again
```
require '.something.php';
include '.something.php';
```
---
## Variables
```
$startsWithDollar;
```
### Constatns doesn't
```
const CONSTANT = 'const_value';
```
### References
```
$a = 5; $b = &$a;
$b = 1; echo $a;
```
### Determine, whether the variable exits.
```
isset($array['1']['2']['3']); // false
```
### Compare variable with null;
```
is_null($array['1']['2']['3']); // false 
// PHP Notice:  Undefined variable: array in /../sth.php on line x 
```
---
## Data Types Recognition
```
is_numeric($x)? "numeric\n" : "";
is_float($x)? "float\n" : "";
is_bool($x)? "bool\n" : "";
is_array($x)? "array\n" : "";
is_string($x)? "string\n" : "";
is_integer($x)? "numeric\n" : "";
is_object($x)? "numeric\n" : "";
```

## Strings
### Replace substring (delete spaces)
```
$myString = str_replace ( ' ', '', $myString);
```
### Deletion of last character
```
$string = substr_replace($string ,"", -1);
```
---
## Arrays
### Creation with brackets
```
$letters = [1,2,3,4,5];
```
### Creation with keyword
```
$aa = array(12,343,523,235,235,45);
```
### Addition at next index of array
```
$array[]= $nextElement;
```
#### a bit faster is
```
array_push($array, $nextElement);
```
### Remove last item from array
```
array_pop($arr);
```
### Index -1 isn't the last, makes ERROR
```
echo $aa[-1]."\n";
```
### Create array from string
```
$list = explode("\n", $input);
```
### and string from array
```
$string = implode("\n",$value);
```
### Sort the array by the keys
```
$array = ksort($array, sorttype);
```
### Determin, whether an array contain the key
```
var_dump( array_key_exists($array_key, $array_name) );
```
### Sum all values of the $array
```
$sum = array_sum($array);
```
---
## Conditions
### Ternary operator
```
$var = is_numeric($x)? "numeric\n" : "";
```
---
## Loops
### Foreach
```
foreach ($array as $key => $value) {
    echo $array[$key] == $value;
}
```
### Doesn't work with string
```
foreach ($string as $letter) {
    echo "Next letter is: ".$lettter."\n";
};
```
---
## Time Measuring
```
$start = microtime(true);
// Any code here ...
$time_elapsed_secs = microtime(true) - $start;
echo "Any code took: $time_elapsed_secs s\n";
```
---
## Assertions
### Needs to set zend.assertions = 1 at php.ini file
you can find it via php -ini (I had it there   /etc/php/7.2/cli/php.ini)
```
assert($a === 1, '$a is not 1');
```
---
## PHP init file
```
/etc/php/7.2/cli/php.ini
```
---
``` 10/11/2019, Jaroslav Langer```
