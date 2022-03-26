"""
sources:

    EPI in Python + own examples

    https://docs.python.org/3/library/bisect.html

        This module provides support for maintaining a list in sorted order
        without having to sort the list after each insertion.
        
        For long lists of items with expensive comparison operations,
        this can be an improvement over the more common approach.

        The module is called `bisect`
        because it uses a basic bisection algorithm to do its work.
        The source code may be most useful as a working example of the algorithm
        (the boundary conditions are already right!).
"""

A = [0, 2, 4, 4, 8, 16]

print()
print("min(A)")
print(min(A))  # 0

print()
print("max(A)")
print(max(A))  # 16


# fmt: off
'''
using `zip` to iterate over two lists of different lengths
'''
# fmt: on
B = [0, 3, 9]
zip_A_B = [(a, b) for a, b in zip(A, B)]

print()
print("A")
print(A)  # [0, 2, 4, 4, 8, 16]
print("B")
print(B)  # [0, 3, 9]
print("zip_A_B")
print(zip_A_B)  # [(0, 0), (2, 3), (4, 9)]


# fmt: off
'''
Reverse a list.
'''
# fmt: on
A_reversed_iterator = reversed(A)
print()
print("A_reversed_iterator")
print(A_reversed_iterator)  # <list_reverseiterator object at 0x7fe85ce61550>
print([x for x in A_reversed_iterator])  # [16, 8, 4, 4, 2, 0]

A.reverse()  # in-place
print()
print("after in-place reversal, A")
print(A)  # [16, 8, 4, 4, 2, 0]

# fmt: off
'''
Sort a list.
'''
# fmt: on
A_sorted_copy = sorted(A)
print()
print("A_sorted_copy")
print(A_sorted_copy)  # [0, 2, 4, 4, 8, 16]
print("A")
print(A)  # [16, 8, 4, 4, 2, 0]

A.sort()  # in-place
print()
print("A")
print(A)  # [0, 2, 4, 4, 8, 16]

# fmt: off
'''
Delete one or multiple items/entries from a list.
'''
# fmt: on
del A[1]
print()
print("after deleting A[1], A")
print(A)  # [0, 4, 4, 8, 16]

del A[1:3]
print()
print("after deleting A[1:3], A")
print(A)  # [0, 8, 16]
