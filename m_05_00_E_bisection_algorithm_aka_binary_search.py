# fmt: off
'''
binary search for a sorted list
'''
# fmt: on
import bisect

# indices
#    0  1  2  3  4  5
A = [0, 2, 4, 4, 8, 16]

x = 4

# fmt: off
'''
Return the index of the first entry in A that is >= x.
(If all elements in the list are < x, the returned values is len(A).)

---

Locate the insertion point for x in A to maintain sorted order.

If x is already present in A,
the insertion point will be before (to the left of) any existing entries.

    The returned insertion point i partitions the array A into two halves so that
        all(val < x for val in A[lo : i])
        for the left side
    and
        all(val >= x for val in A[i : hi])
        for the right side.

The return value is suitable for use as the first parameter to `A.insert()`
assuming that A is already sorted.
'''
# fmt: on

print()
print("bisect.bisect_left(A, x)")
print(bisect.bisect_left(A, x))  # 2

# fmt: off
'''
Return the index of the first entry in A that is > x.
(If all elements in the list are <= x, the returned value is len(A).)

---

Similar to bisect_left(),
but returns an insertion point
which comes after (to the right of) any existing entries of x in a.

    The returned insertion point i partitions the array A into two halves so that
        all(val <= x for val in A[lo : i]) for the left side
    and
        all(val > x for val in A[i : hi]) for the right side.
'''
# fmt: on
print()
print("bisect.bisect_right(A, x)")
print(bisect.bisect_right(A, x))  # 4

print()
print("bisect.bisect(A, x)")
print(bisect.bisect(A, x))  # 4
