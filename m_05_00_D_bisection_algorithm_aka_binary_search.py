# fmt: off
'''
binary search for a sorted list
'''
# fmt: on
import bisect


# fmt: off
'''
bisect = bisect_right

Return the index of the first entry in A that is > x.
(If all elements in the list are <= x, the returned value is len(A).)
'''
# indices
#      0    1    2    3  4
B = [0.0, 0.5, 0.8, 0.9, 1]

print()

idx = bisect.bisect(B, 0.3)  # 1
print(idx)
idx = bisect.bisect(B, 0.5)  # 2
print(idx)
idx = bisect.bisect(B, 0.6)  # 2
print(idx)
idx = bisect.bisect(B, 0.85)  # 3
print(idx)
idx = bisect.bisect(B, 0.95)  # 4
print(idx)

idx = bisect.bisect(B, -1)  # 0
print(idx)

# fmt: off
'''
Return the index of the first entry in A that is >= x.
(If all elements in the list are < x, the returned values is len(A).)
'''

# indices
#    0  1  2  3   4
C = [int(b * 10) for b in B]
#   [0, 5, 8, 9, 10]

print()

idx = bisect.bisect_left(C, 3)  # 1
print(idx)
idx = bisect.bisect_left(C, 5)  # 1  (diff from prev example!)
print(idx)
idx = bisect.bisect_left(C, 6)  # 2
print(idx)
idx = bisect.bisect_left(C, 8.5)  # 3
print(idx)
idx = bisect.bisect_left(C, 9.5)  # 4
print(idx)

idx = bisect.bisect_left(C, -10)  # 0
print(idx)
