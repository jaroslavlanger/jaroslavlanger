<?php

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

class Seat extends Car {
    
    public function readSeats()
    {
        echo "The Seat has ".$this->seats." seats.\n";
    }
}

$car1 = new Car(4);

$car1->countSeats();
# int(4)

$car2 = new Seat(5);

$car2->countSeats();
# int(5)

$car2->readSeats();
# The Seat has 5 seats.