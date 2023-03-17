<?php

use App\Stamgast;

class StamgastTest extends \PHPUnit\FrameWork\TestCase
{
    protected $stamgast;

    public function setUp()
    {
        $this->samgast = new Stamgast();
    }

    public function testGetSet()
    {
        $this->stamgast->setJmeno('Bedrich');
        
    }
}