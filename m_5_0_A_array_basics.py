"""
sources:

    https://docs.python.org/3/tutorial/datastructures.html

    EPI in Python + own examples



Arrays in Python are provided by the `list` type.

The key property of a `list` is that it is dynamically-resized,
i.e. there's no bound as to how many elements can be added to it.
"""

# fmt: off
'''
Instantiate a list.
'''
# fmt: on
A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print()
print("A")
print(A)

# fmt: off
'''
Get the length of A.
'''
# fmt: on
print()
print("len(A)")
print(len(A))

# fmt: off
'''
Append an item/entry to the right.

    Equivalent to a[len(a):] = [x].
'''
# fmt: on
A.append(42)

print()
print("after appending 42 to the right of A")
print(A)

# fmt: off
'''
Remove an item/entry.

    Remove the first item/entry from the list whose value is equal to x.
    It raises a ValueError if there is no such item/entry.
'''
# fmt: on
A.remove(7)

print()
print("after removing 7 from A")
print(A)

# fmt: off
'''
Insert an item/entry at a given position.

    The first argument is the index of the element before which to insert, so

        `A.insert(0, x)` inserts at the front of the list,
        
        and `A.insert(len(a), x)` is equivalent to `A.append(x)`.
'''
# fmt: on
A.insert(7, 77)

print()
print("after inserting 77 inot A at index 7")
print(A)
