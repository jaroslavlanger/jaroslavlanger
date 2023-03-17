<?php
class Attachment
{
    const TYPE ='attachment';
    protected static $seq = 0;

    protected $id;
    protected $type;

    public function __construct()
    {
        $this->id = ++self::$seq;
        $this->type = static::TYPE;
    }   
    public function __toString()
    {
        return "{$this->id}: {$this->type}";
    }

}