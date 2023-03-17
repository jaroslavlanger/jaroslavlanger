<?php

spl_autoload_register(function ($className){
    require __DIR__.'/src/'.$className.'.php';
});

$p1 = new Product();
$p1
    ->setId(1)
    ->setName('Guma')
    ->setPrice(199);

$p2 = new Product();
$p2
    ->setId(2)
    ->setName('Amug')
    ->setPrice(991);

$c = new Customer;
$c
    ->setId(1)    
    ->setName('Alois');

$o = new Order();
$o
    ->setCustomer($c)
    ->setCreated(new \DateTime())
    ->setItem($p1)
    ->setItem($p1);

var_dump($p1, $p2);