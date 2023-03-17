# General goods for PHP

## MENU
+ [Namespaces](#namespaces)
+ [Autoloading](#autoloading)
+ [Error handling](#error-handling)
+ [Work with files](#work-with-files)
+ [Work with JSON](#work-with-json)

## Namespaces
//TODO

## Autoloading
Load all classes correctly can be quite painful, autoloading may help.

### Without namespaces

When you write something like:
```
$obj = new Class1();
```
You needed to require or include the Class1 in a way similar to:
```
require_once './path/you/desire/Class1.php';
```
For one require it is perfect but when you need to require dozen of classes much nicer is to use this block:
```
spl_autoload_register(function ($className){
    require __DIR__.'/path/you/desire/'.$className.'.php';
});
```
Once the interpret reaches Class1 in code, it will automaticly search for ./path/you/desire/Class1.php

### With namespaces
When using namespaces (highly recommended) the interpret will reach something like:
```
$obj = new Namespace1\Namespace2\Class1();
```
#### In case of UNIX like system
(where for directories is used separator '/')

You only need to replace the backslashes from namespace with slashes and it will work fine again.
```
spl_autoload_register(function($className) {
    require __DIR__.'/path/you/desire/'.str_replace('\\', '/', $className).'.php';
});
```
---
## Error handling
https://stackoverflow.com/questions/5683592/phpunit-assert-that-an-exception-was-thrown
https://www.php.net/manual/en/book.errorfunc.php

## Work with files
### Write to file
```
file_put_contents ( './myNewFile.json', '{ "number", "1" }', FILE_APPEND ); 
//file_put_contents ( string $filename , mixed $data [, int $flags = 0 [, resource $context ]] ) 
```
[source](https://www.php.net/manual/en/function.file-put-contents.php)
### Read file
Into array
```
```
Into string 
```
file_get_contents

```
[source](https://www.php.net/manual/en/function.file-get-contents.php)

## Work with JSON
### encode
```
```
### decode
```
json_decode ( string $json [, bool $assoc = FALSE [, int $depth = 512 [, int $options = 0 ]]] ) : mixed
```
https://www.php.net/manual/en/function.json-decode.php

```10/11/2019, Jaroslav Langer```