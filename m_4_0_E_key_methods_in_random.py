"""
source for docstrings: https://docs.python.org/3/library/random.html
source for examples: EPI in Python + own examples
"""

import random

# fmt: off
'''
random.randrange(stop)
random.randrange(start, stop[, step])

    Return a randomly selected element from range(start, stop, step).
'''
# fmt: on
print()
print("random.randrange(28)")
print(random.randrange(28))

# fmt: off
'''
random.randint(a, b)

    Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
'''
# fmt: on
print()
print("random.randint(8, 16)")
print(random.randint(8, 16))

# fmt: off
'''
random.random()

    Return the next random floating point number in the range [0.0, 1.0).
'''
# fmt: on
print()
print("random.random()")
print(random.random())

# fmt: off
'''
random.shuffle(x[, random])

    Shuffle the sequence x in place.

    Note that even for small len(x),
    the total number of permutations of x can quickly grow larger than
    the period of most random number generators.
    This implies that most permutations of a long sequence can never be generated.
    For example, a sequence of length 2080 is the largest
    that can fit within the period of the Mersenne Twister random number generator.

    Deprecated since version 3.9, will be removed in version 3.11:
    The optional parameter random.
'''
# fmt: on
A = [1, 2, 3, 4, 5, 6, 7]
print()
print("random.shuffle(A)")
print(random.shuffle(A))  # None
print("A")
print(A)

# fmt: off
'''
random.choice(seq)

    Return a random element from the non-empty sequence seq.
    If seq is empty, raises IndexError.
'''
# fmt: on
print()
print("random.choice(A)")
print(random.choice(A))
