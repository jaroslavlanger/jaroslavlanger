# Rucursion 

Can be incredibely efficient way to write a code. Visible on following example.

## Creation of Iterator in PHP (Tree traversals)

```
<?php

namespace Iterator;

use Node;

abstract class AbstractOrderIterator implements \Iterator
{
    protected $root;
    protected $current;
    protected $stack = [];

    public function __construct(Node $root)
    {
        $this->root = $root;
    }

    public function current()
    {
        return $this->current;
    }

    public function next()
    {
        $this->current = array_pop($this->stack);
    }

    public function valid()
    {
        $valid = !is_null($this->current);
        return $valid;
    }

    public function rewind()
    {   
        $this->getStacked($this->root);
        $this->current = array_pop($this->stack);
    }
}
```

### InOrder traversal

#### Without recursion
```
class InOrderIterator extends AbstractOrderIterator {

    protected function leftest(Node $node)
    {   
        $left = $node->getLeft();
        while(!is_null($left)){
            array_push($this->stack, $node);
            $node = $left;
            $left = $node->getLeft();
        }
        return $node;
    }

    public function next()
    {   
        $right = $this->current->getRight();
        if(!is_null($right)){
            $this->current = $this->leftest($right);
        } else {
            $this->current = array_pop($this->stack);
        }
    }

    public function rewind()
    {
        $this->current = $this->leftest($this->root);
    }
}
```
#### With recursion
```
class InOrderIterator extends AbstractOrderIterator {

    protected function getStacked($node)
    {
        if(is_null($node)){
            return;
        }
        $this->getStacked($node->getRight());
        array_push($this->stack, $node);
        $this->getStacked($node->getLeft());
    }
}
```
### Pre-Ordred traversal

#### Without recursion
```
class PreOrderIterator extends AbstractOrderIterator {

    public function next()
    {   
        $right = $this->current->getRight();
        if(!is_null($right)){
            array_push($this->stack, $right);
        }
        $left = $this->current->getLeft();
        if(!is_null($left)){
            $right = $this->current->getRight();
            $this->current = $left;
        } else {
            $this->current = array_pop($this->stack);
        }
    }
    
    public function rewind()
    {   
        $this->current = $this->root;
    }
```
#### With recursion
```
class PreOrderIterator extends AbstractOrderIterator {

    protected function getStacked($node)
    {
        if (is_null($node)) {
            return;
        }
        $this->getStacked($node->getRight());
        $this->getStacked($node->getLeft());
        array_push($this->stack, $node);
    }
}
```

### Pre-Ordred traversal

#### Without recursion

**? ? ?**

#### With recursion
```
class PostOrderIterator extends AbstractOrderIterator
{

    protected function getStacked($node)
    {
        if(is_null($node)){
            return;
        }
        array_push($this->stack, $node);
        $this->getStacked($node->getRight());
        $this->getStacked($node->getLeft());
    }
}
```