# Self-taught-Python

Keep track of Python learning process by inclduding works and experimental codes store into the repository to collaborate with friends for improvement.

## Building Socket Server

Use [socket](https://docs.python.org/3/library/socket.html) modules to build own sockets.

## Object Oriented Programming (OOP)

* Two important aspects of OOP: inheritance & composition
* Three distinct differences from modules: multiple instances, customization via inheritance, operator overloading
* Both classes and modules are namespaces for attaching attributes but a class is a statement within a file while module reflects an entire file
* OOP expression in Python: `object.attribute`
* Two types of OOP object: class objects & instance objects
  * class objects - shared by all instances; default behaviors
  * instance objects - owned by the instance only and vary for different instances
* `__init__` is the most common operator overloading method known as constructor for initializing object' state

### Simplify OOP processes

1. Use `class` statement to generate class object
2. instance object is created when class is called
3. instances linked all classes above it, i.e., subclasses
4. subclasses then linked all superclasses as from bottom-to-top approach in left-to-right order

### Common Operator Overloading

* `__base__` - look for object's superclass of an instance
* `__class__` - look for object's class of an instance
* `__dict__` - look for class object's attributes of an instance

## Keyword Concepts

* class - design to create and manage new objects & support *inheritance*
* inheritance - mechanism of code customization & reuse
* strategic mode - long-term product development
* tactical mode - for short-supply
* methods - functions attached to classes as attributes
* polymorphism - care what it does and not what it is
