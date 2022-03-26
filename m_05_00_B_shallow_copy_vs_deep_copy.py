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

import copy

A = [0, 2, 4, 8]

A_shallow_copy_implicit = A
A_shallow_copy_explicit = copy.copy(A)

A_deep_copy_implicit = list(A)
A_deep_copy_explicit = copy.deepcopy(A)

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
print()
print(
    fmt_str.format(
        "A_shallow_copy_implicit",
        A_shallow_copy_implicit,
        removed_value in A_shallow_copy_implicit,
    )
)
print(
    fmt_str.format(
        "A_shallow_copy_explicit",
        A_shallow_copy_explicit,
        removed_value in A_shallow_copy_explicit,
    )
)
print()
print(
    fmt_str.format(
        "A_deep_copy_implicit",
        A_deep_copy_implicit,
        removed_value in A_deep_copy_implicit,
    )
)
print(
    fmt_str.format(
        "A_deep_copy_explicit",
        A_deep_copy_explicit,
        removed_value in A_deep_copy_explicit,
    )
)
