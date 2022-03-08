import collections

c = collections.Counter(a=3, b=1)
d = collections.Counter(a=1, b=2)

print()
print("c:")
print(c)  # Counter({'a': 3, 'b': 1})
print("d:")
print(d)  # Counter({'b': 2, 'a': 1})

# Add 2 `Counter`s together.
# (That "returns" c[x] + d[x].)
print()
print("Add 2 `Counter`s together.")
print("c + d:")
print(c + d)  # Counter({'a': 4, 'b': 3})

# Subtract 2 `Counter`s.
# (The following "returns" c[x] - d[x] _but keeps only the positive results.)
print()
print("Subtract 2 `Counter`s.")
print("c - d:")
print(c - d)  # Counter({'a': 2})

# Intersect 2 `Counter`s.
# (That "returns" min(c[x], d[x]).)
print()
print("Intersect 2 `Counter`s.")
print("c & d:")
print(c & d)  # Counter({'a': 1, 'b': 1})

# Compute the union of 2 `Counter`s.
# (That "returns" max(c[x], d[x]).)
print()
print("Compute the union of 2 `Counter`s.")
print("c | d:")
print(c | d)  # Counter({'a': 2, 'b': 2})
