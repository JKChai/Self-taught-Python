# Self-taught-Python

Keep track of Python learning process by inclduding works and experimental codes store into the repository to collaborate with friends for improvement.

Below are some notes taken from the author's learning journey and is intended to help support the author itself and not for others.

## Building Socket Server

Use [socket](https://docs.python.org/3/library/socket.html) modules to build own sockets.

---

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
* Parent `class` is inherited by being called by a child `class` where child `class` have accesed to all parents data 
```python
class child(parent):
  # do something
```
* Inheritance is being defined by DataCamp as "is-a" relationship, e.g., a child class is a parent class. This is saying that the instance of a child class is also an instance of parent class because this child class' instance inherited all parent class properties.

### Simplify OOP processes

1. Use `class` statement to generate class object
2. instance object is created when class is called
3. instances linked all classes above it, i.e., subclasses
4. subclasses then linked all superclasses as from bottom-to-top approach in left-to-right order

### Common Operator Overloading

* `__base__` - look for object's superclass of an instance
* `__class__` - look for object's class of an instance
* `__dict__` - look for class object's attributes of an instance

#### Comparison

* Use for comparing 2 objects

| Operator | Method |
|----|----|
| `==` | `__eq__()` |
| `!=` | `__ne__()` |
| `>=` | `__ge__()` |
| `<=` | `__le__()` |
| `>` | `__gt__()` |
| `<` | `__lt__()` |

* `__hash__()` method for comparing dictionary key objects

#### String representation

* `__str__()` - informal, for end user (string representation)
* `__repr__()` - formal, for developer (reproducible representation)

### Custom Exceptions

* For Developers not users, can be done with inheritance, e.g.,
```python
class BaseError(ValueError):
  pass
```
* `raise` keyword terminates the program after returning the given message or object

> It's better to include an except block for a child exception before the block for a parent exception, otherwise the child exceptions will be always be caught in the parent block, and the except block for the child will never be executed.

### Design Principles

* Idea - Interface is all that matters
* OOP should design to handle polymorphism; the bottom line is if LSP is violated, the class object should not use inheritance
> **Liskov Substitution Principle**
>> Base class should be interchangeable with any of its subclasses without altering any properties of the program 

#### Private Attributes

* naming conventions - leading `_` is for internal details of implementation while leading `__` are used for attributes that should not be inherited to avoid name clashes in child classes

#### Properties

* Control attribute access including checking the validity of the values or make attributes read-only
* Use `@property` decorator for built-in access control and uses provide methods `@attr.setter`, `@attr.getter`, & `@attr.deleter` for modifying, retrieving, and deleter purposes

### More & More

#### Functionality

* Multiple inheritance & mixin classes
* Overriding built-in operators like `+`
* `__getattr__()` and `__setattr__()`
* Custom iterators
* Abstract base classes
* Dataclasses

#### Design

* *SOLID* Principles
 * Single-responsibility principle
 * Open-closed principle
 * Liskov substitution principle
 * Interface segregation principle
 * Dependency inversion principle

---

## Introduction to Airflow

* Airflow is a platform to program workflows
* Use for Creating, Scheduling, and monitoring data workflow

* E.g.,
```bash
## Executing Task using airflow run command
## airflow run <dag_id> <task_id> <start_date>
airflow run etl_pipeline download_file 2020-01-08
```

* DAG (Airflow Context) - Directed Acyclic Graphs that represents the set of tasks that make up your workflow
 * Directed - An inherent flow representing depencies between components
 * Acyclic - Does not loop/cycle/repeat
 * Graph - Represent components and the relationships (or depencies) between them

* When to use Command Line VS Python?
| Command Line | Python |
|----|----|
| Start Airflow Processes | Create a DAG |
| Manually Run DAGs/Tasks | Edit individual/properties of a DAG |
| Get Logging info from Airflow | |

---

## Keyword Concepts

* class - design to create and manage new objects & support *inheritance*
* inheritance - mechanism of code customization & reuse
* encapuslation - bundling data with methods that operate on data
* strategic mode - long-term product development
* tactical mode - for short-supply
* methods - functions attached to classes as attributes
* polymorphism - care what it does and not what it is
* Data Engineer - Taking any action involving data and turning into something reliable, repetable, and maintainable process
