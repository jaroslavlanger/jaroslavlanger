# Functions in PHP

## MENU

+ [Arguments](#arguments)
+ [Built-in functions](#built-in-functions)
+ [REGEX](#regex)

---
## Arguments
### Passing like a reference
```
function swap(&$a, &$b){
    $b = $b + $a;
    $a = $b - $a;
    $b = $b - $a; 
}
```
### passing any number of arguments
```
function vanish($string, ...$useless){
    foreach ($useless as $use => $less) {
    }
    return $string;
}
```
---
## Built-in functions
### Random number function
```
$num = rand(10,99);
```
---
## REGEX
### Match case 
```
$subject = "abcdef";
$pattern = '/def/';
preg_match($pattern, $subject, $matches);
print_r($matches); // [ "def" ]
```
### Splitting
```
$string = "1+2-3";
$array = preg_split('/[+-]/', $string);
print_r($array);    // [1, 2, 3]
```

### Price examples
```
const INTS = '[[:digit:]]{1,3}(\.[[:digit:]]{3})*';
const FLOATS = INTS.'(,[[:digit:]]*)?';
const PRICE = '/'.INTS.'(\ )*,-/';
const KC = '/'.FLOATS.'(\ )*Kč/';
const CZK = '/(CZK(\ )*'.FLOATS.')|('.FLOATS.'(\ )*CZK)/';
```
---
```10/11/2019, Jaroslav Langer```
