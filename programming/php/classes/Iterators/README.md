# Iterators

Iterators are the things you use with foreach or for x in y.

## How to create your own iterator

[The Iterator interface](https://www.php.net/manual/en/class.iterator.php)

## How to just call foreach($object as $value)

[The IteratorAggregate interface](https://www.php.net/manual/en/class.iteratoraggregate.php)

## Hash table is often the most efficient way to store and access data

Function for hashing all the objects
[spl_object_hash](https://www.php.net/manual/en/function.spl-object-hash.php)
! careful, it can not hash the primitive types !