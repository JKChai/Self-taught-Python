# Self-taught-Python

Keep track of Python learning process by inclduding works and experimental codes store into the repository to collaborate with friends for improvement.

Below are some notes taken from the author's learning journey and is intended to help support the author itself and not for others.

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
* "Classes and objects both have attributes and methods, but the difference is that a class is an abstract template, while an object is a concrete representation of a class."
 * E.g., `Object.method(attribute)` will be interpreted as `Class.method(Object, attribute)`
* Class-level VS Instance-level data
 * Class-level data such as class attributes are global constants in a class
 * e.g., no `self` involved and is shared accross instance-level data
* class method, represented by decorator `@classmethod`, cannot use instance-level data and take `cls` like `self` as the first argument for the function during initialization to represent the class itself; the main use-case for class method is for alternative construtors.
* static method, represented by decorator `@staticmethod`, does not receive an implicit first argument and can be called on class, instance, and by itself as a regular function; the purpose of this method is to avoid the automatic transformation to instance method when reference to a function from a class body is needed.

### Class inheritance

* To fullfill DRY (Don't repeat yourself) & all about code reuse

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
* encapuslation - bundling data with methods that operate on data
* strategic mode - long-term product development
* tactical mode - for short-supply
* methods - functions attached to classes as attributes
* polymorphism - care what it does and not what it is
