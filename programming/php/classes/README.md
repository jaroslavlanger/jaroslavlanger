# Classes PHP

```<?php```

## Class definition

```
class Car {
    
    // Accesible only from this class or from child.
    protected $seats;
    
    // Constructor
    public function __construct($number)
    {
        $this->seats = $number;
    }

    public function countSeats()
    {
        var_dump($this->seats);
    }
}
```

## Inheritance
```
class Seat extends Car {
    
    public function readSeats()
    {
        echo "The Seat has ".$this->seats." seats.\n";
    }
}
```

## Creation of cars

```
$car1 = new Car(4);

$car1->countSeats();
# int(4)

$car2 = new Seat(5);

$car2->countSeats();
# int(5)

$car2->readSeats();
# The Seat has 5 seats.
```

### Atribut referencing 
Mind, that the dollar for variable is used only once, correctly:
```$this->seat_number = 5;```
**not**
```$this->$seat_number = 5;```
It's the same with calling functions.

## Setters

As you MIGHT use setters
```
public function setLeft(?Node $left): Node
    {
        $this->left = $left;

        return $this;
    }
```
### There is a shortcut for setting all the values while creation:

(It's possible as the setters returns ```$this```)
```
$tree1 = (new Node(1))
	->setLeft((new Node(2))
		->setLeft(new Node(4))
		->setRight(new Node(5))
	)
	->setRight(new Node(3));
```
Comparing to 
```
$tree1 = new Node(1);
$tree2 = new Node(2);
$tree2->setLeft(new Node(4));
$tree2->setRight(new Node(5));
$tree1->setLeft($tree2);
$tree1->setRight(new Node(3));
```
---
31/10/2019, Jaroslav Langer 
