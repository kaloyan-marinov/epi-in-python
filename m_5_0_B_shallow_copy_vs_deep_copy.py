"""
sources:

    https://docs.python.org/3/library/copy.html

    EPI in Python + own examples

Assignment statements in Python do not copy objects,
they create bindings between a target and an object.
For collections that are mutable or contain mutable items,
a copy is sometimes needed so one can change one copy without changing the other.

This module provides generic shallow and deep copy operations (explained below).

The difference between shallow and deep copying is only relevant for compound objects
(objects that contain other objects, like lists or class instances):

    A _shallow copy_ constructs a new compound object
    and then (to the extent possible) inserts _references_ into it to the objects
    found in the original.

    A _deep copy_ constructs a new compound object
    and then, recursively, inserts _copies_ into it of the objects
    found in the original.
"""

A = [0, 2, 4, 8]

B = A
C = list(A)

A.remove(4)
removed_value = 4

fmt_str = "{0:<25} {1!s:<25} {2:<30}"

print()

print(
    fmt_str.format(
        "name of arr variable",
        "value of arr variable",
        f"is {removed_value} in [name of arr variable]?",
    )
)

print(fmt_str.format("-" * 25, "-" * 25, "-" * 30))
print(fmt_str.format("A", A, removed_value in A))
print(fmt_str.format("B", B, removed_value in B))
print(fmt_str.format("C", C, removed_value in C))
