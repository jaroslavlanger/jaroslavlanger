<?php
/**
 * 
 */
trait IdTrait
{
    protected static $seq = 0;

    /** @var int */
    protected $id;

    public function generateId()
    {
        $this->id = ++self::$seq;
    }

    /**
     * Get the value of id
     */ 
    public function getId()
    {
        return $this->id;
    }

    public function __construct()
    {
        $this->generateId();
    }

}
