# OOP

- a way of structuring code to promote reusability and organization
- uses objects that bundle data AND behavior together
- objects are instances of a class
- classes are blueprints or archetypes for creating and describing objects

## OOP Pillars
- Encapsulation: data and behavior are bundled inside the object, privacy access to information
- Inheritance: allows a class (child/derived) to inherit EVERYTHING from a parent class (base class) -> class-based multiple inheritance
- Abstraction: hides complex details while exposing only what's necessary
- Polymorphism: allows objects of different classes to be treated as instances of the same class through a common interface

## OOP Design Principles
- SoC: Separation of Concerns
- DRY: Do not Repeat Yourself
- SOLID: 
    - SRP: Single Responsibility Principle
    - Open/Closed Principle: software should be open for extension but closed for modification
    - Liskov's Substitution Principle: subclasses can be substituted with their base class without changing the correctness of the program
    - Interface Segregation Principle: a class should not be forced to build methods it doesn't use
    - Dependency Inversion Principle: high-level modules should not depend on low-level modules but rather on abstractions

## OOP Design Patterns
- Decorator Pattern: structural pattern that adds behavior to an object dynamically