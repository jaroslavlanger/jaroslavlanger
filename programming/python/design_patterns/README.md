# Design Patterns in Python

Kind of smallest examples of design patterns in python.

<!-- TOC GFM -->

* [Builder](#builder)
* [Factory](#factory)
* [Prototype](#prototype)
* [Singleton](#singleton)
* [Adapter](#adapter)
* [Bridge](#bridge)
* [Composite](#composite)
* [Decorator](#decorator)
* [Facade](#facade)
* [Flyweight](#flyweight)
* [Proxy](#proxy)
* [Chain of Responsibility](#chain-of-responsibility)
* [Command](#command)
* [Interpreter](#interpreter)
* [Iterator](#iterator)
* [Mediator](#mediator)
* [Memento](#memento)
* [Observer](#observer)
* [State](#state)
* [Strategy](#strategy)
* [Template Method](#template-method)
* [Visitor](#visitor)

<!-- /TOC -->

The code was written as a solution to coding exercises of [Design Patterns in Python Udemy course by Dmitri Nesteruk](https://www.udemy.com/course/design-patterns-python/#instructor-1),  which I recommend.

Follows a list of design patterns with one-liners from Dmitri.

## Builder

When piecewise object construction is complicated provide an API for doing it succinctly.

## Factory

A component responsible solely for the wholesale (not piecewise) creation of objects.

## Prototype

A partially or fully initialized object that you copy (clone) and make use of.

## Singleton

A component which is instantiated only once.

## Adapter

A construct which adapts an existing interface X to conform to the required interface Y.

## Bridge

A mechanism that decouples and interface (hierarchy) from an implementation (hierarchy).

## Composite

A mechanism for treating individual (scalar) objects and compositions of objects in a uniform manner.

## Decorator

Facilitates the addition of behaviors to individual objects without inheriting from them.

## Facade

Provides a simple, easy to understand user interface over a large and sophisticated body of code.

## Flyweight

A space optimization technique that lets us use less memory by storing externally the data associated with similar objects.

## Proxy

A class that functions as an interface to a particular resource. That resource may be remote, expensive to construct, or may require logging or some other added functionality.

## Chain of Responsibility

A chain of components who all get a chance to process a command or a query, optionally having default processing implementation and an ability to terminate the processing chain.

## Command

An object which represents an instruction to perform a particular action. Contains all the information necessary for the action to be taken.

## Interpreter

A component that processes structured text data. Does so by turning it into separate lexical tokens (lexing) and then interpreting sequences of said tokens (parsing).

## Iterator

An object that facilitates the traversal of a data structure.

## Mediator

A component that facilitates communication between other components without them necessarily being aware of each other or having direct (reference) access to each other.

## Memento

A token/handle representing the system state. Lets us roll back to the state when the token was generated. May or may not directly expose state information.

## Observer

An observer is an object that wishes to be informed about events happening in the system. The entity generating the events is an observable.

## State

 A pattern in which the object's behavior is determined by its state. An object transitions from one state to another (something needs to trigger a transition).

A formalized construct which manages state and transitions is called a state machine.

## Strategy

Enables the exact behavior of a system to be selected at run-time.

## Template Method

Allow us to define the 'skeleton' of the algorithm, with concrete implementations defined in subclasses.

## Visitor

A component (visitor) that knows how to traverse a data structure composed of (possibly related) types.
