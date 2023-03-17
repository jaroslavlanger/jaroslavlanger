<?php

class Order
{
    /** @var int */
    protected $id;

    /** @var date */
    protected $created;

    /** @var date */
    protected $ordered;
    
    /** @var Customer */
    protected $customer;

    /** @var Product[] */
    protected $items;

    public function addItem($item){
        $this->items[] = $item;
            return $this;
    }

    public function removeItem($item){
        foreach ($this->items as $key=>$item) {
            if($item === $remove){
                unset($this->$items[$key]);
            }
        }
        return $this; 
    }

    /**
     * Get the value of created
     */ 
    public function getCreated()
    {
        return $this->created;
    }

    /**
     * Set the value of created
     *
     * @return  self
     */ 
    public function setCreated($created)
    {
        $this->created = $created;

        return $this;
    }

    /**
     * Get the value of ordered
     */ 
    public function getOrdered()
    {
        return $this->ordered;
    }

    /**
     * Set the value of ordered
     *
     * @return  self
     */ 
    public function setOrdered($ordered)
    {
        $this->ordered = $ordered;

        return $this;
    }

    /**
     * Get the value of customer
     */ 
    public function getCustomer()
    {
        return $this->customer;
    }

    /**
     * Set the value of customer
     *
     * @return  self
     */ 
    public function setCustomer($customer)
    {
        $this->customer = $customer;

        return $this;
    }

    /**
     * Get the value of items
     */ 
    public function getItems()
    {
        return $this->items;
    }

    /**
     * Set the value of items
     *
     * @return  self
     */ 
    public function setItems($items)
    {
        $this->items = $items;

        return $this;
    }
}
