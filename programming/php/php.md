# PHP

`2021 Feb 21, Jaroslav Langer`

## Contents

<!-- TOC GFM -->

* [TODO](#todo)
* [Basics](#basics)
* [syntax](#syntax)
    * [Comments](#comments)
* [Proměnné](#promnné)
    * [možnost pojmenovat proměnou pomocí proměnné i u funkcí](#monost-pojmenovat-promnou-pomocí-promnné-i-u-funkcí)
    * [Viditelnost proměnných](#viditelnost-promnných)
* [Reference](#reference)
* [Konstanty](#konstanty)
    * [Statické proměnné](#statické-promnné)
    * [Superglobální pole](#superglobální-pole)
* [Funkce pro práci s proměnnými](#funkce-pro-práci-s-promnnými)
* [Data Types](#data-types)
* [String](#string)

<!-- /TOC -->

## TODO

* General/Namespaces
* https://stackoverflow.com/questions/45965699/mocks-vs-stubs-in-phpunit
* https://www.geeksforgeeks.org/php-gettype-function/
* printr
* clone
* Linux days

* **Composer**
```
mv composer.phar /usr/local/bin/composer
```
* [source](https://getcomposer.org/doc/00-intro.md)

* **Unit tests**
```
sudo apt-get install php-xml
sudo apt-get install php-mbstring
```

## Basics

* skriptovací, interpretovaný (facebook to nějak umí)
* php = ~personal homepages~
* dynamicky typovaný
* možná práce s lokálním systémem
* možné #! cestu k interpretru a pouštět v shellu

## syntax

\<?php a ?>

* otevírací značka, aby se oddělil od html
    * nedoporučuje se mít v jednom souboru
* nedoporučuje se používat uzavírací značku

příkazy se oddělují středníkem
bloky se uzavírají { }

### Comments

//  |  /* */  |  /** * */

## Proměnné

* začínají dolarem
* jsou case sensitivní
* doporučená je malá camelNotace
* nesmí začínat číslem
* inicializace probíhá hodnotou

### možnost pojmenovat proměnou pomocí proměnné i u funkcí

>$promenna = prom
$$promenna = prom2

### Viditelnost proměnných

Proměnné jsou viditelné v bloku kde je a níž

## Reference

&$b = $a

## Konstanty

keyword const
existuji magicke konstanty

### Statické proměnné

drží sí místo v paměti, například pro proměnné ve funci

### Superglobální pole

$_GET $_POST $_COOKIE uspořádané v poli $_REQUEST

**!!! Potenciálně nebezpečné**

## Funkce pro práci s proměnnými

* isset($prom)
* empty
* is_numeric
* is_{bool, inteege, float, string, ...}

* unset() - delete item by index
  * possibility to free the memory

get_class, instaceof

## Data Types

* primitive
* composed

## String
