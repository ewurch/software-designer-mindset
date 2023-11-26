Notes and Things about The Software Designer Mindset Course - ArjanCodes
=======

### Types and Type Hints:

There are two axess of typing:

- Static vs Dynamic:
    Is about when the typing information is required.
    - Static: required at compiling time
    - Dynamic: required at running time

- Weak vs Strong:
    Is about the strictness of the type annotation.
    - Weak: Automatic conversion of integers to strings, for example.
    - Strong: Stricter typing conversion rules.


Different languages use different combinations and graduations of these concepts, Python for example, is a Dynamic and Strong typed language.

There is also another dimension, Nominal vs Structural Typing:
- Nominal: The type of the object is determined by explicit declarations, not considering it's behaviour.
- Structural: The type is derived from the structure of the object, also known as duck typing, `if it walks like a duck, and quacks like a duck, must be a duck`.


### Pure Function and side effects:

Pure functions are functions that the output rely solely on the input values. To test functions that are not pure you need to mock the values that are being expected inside it.
