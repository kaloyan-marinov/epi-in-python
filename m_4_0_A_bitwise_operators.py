"""
source for docstrings: https://wiki.python.org/moin/BitwiseOperators
source for examples: EPI in Python + own examples
"""

# fmt: off
'''
x << y

    Returns x with the bits shifted to the left by y places
    (and new bits on the right-hand-side are zeros).
    This is the same as multiplying x by 2**y.
'''
# fmt: on
print()
print("1 << 10")
print(1 << 10)  # 1024

# fmt: off
'''
x >> y

    Returns x with the bits shifted to the right by y places.
    This is the same as //'ing x by 2**y. 
'''
# fmt: on
print()
print("8 >> 1")
print(8 >> 1)

print()
print("-16 >> -1")
print(-16 >> 1)  # -8

# fmt: off
'''
x & y

    Does a "bitwise and".
    Each bit of the output is 1 if the corresponding bit of x AND of y is 1,
    otherwise it's 0. 
'''
# fmt: on
print()
print("6 & 4")
print(6 & 4)  # 4

# fmt: off
'''
x | y

    Does a "bitwise or".
    Each bit of the output is 0 if the corresponding bit of x AND of y is 0,
    otherwise it's 1. 
'''
# fmt: on
print()
print("1 | 2")
print(1 | 2)  # 3

# fmt: off
'''
~ x

    Returns the complement of x
    - the number you get by switching each 1 for a 0 and each 0 for a 1.
    This is the same as -x - 1. 
'''
# fmt: on
print()
print("~0")
print(~0)  # -1

# fmt: off
'''
x ^ y

    Does a "bitwise exclusive or".
    Each bit of the output is
    the same as the corresponding bit in x if that bit in y is 0,
    and it's the complement of the bit in x if that bit in y is 1. 
'''
# fmt: on
print()
print("15 ^ 11")
print(15 ^ 11)  # 4

print()
print("15 ^ -11")
print(15 ^ -11)  # -6
