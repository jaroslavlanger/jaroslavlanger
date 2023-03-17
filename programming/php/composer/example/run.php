<?php
require 'vendor/autoload.php';

use App\Model\Customer;
use Symfony\Component\Validator\Validation;


require 'vendor/autoload.php';

$alois = new Customer;
$alois
    ->setName('alois')
    ->setAge(16)
    ->setEmail('a@a.aa');

$validator = Validation::createValidatorBuilder()
    ->addMethodMapping('loadValidatorMetadata')
    ->getValidator();

$violations = $validator->validate($alois);

if(0 != count($violations)){
    foreach ($violations as $violation) {
        echo $violation->getPropertyPath().": ".$violation->getMessage()."\n";
    }
} else {
    echo "{$alois->getName()} is OK\n";
}