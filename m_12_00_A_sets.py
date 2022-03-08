# Instantiate a `set`.
s = {1, 2, 3}

print()
print("s:")
print(s)  # {1, 2, 3}

# Add a new element to `s`.
s.add(42)

print()
print("Add a new element to `s`.")
print("s:")
print(s)  # {1, 2, 3, 42}

# Remove an element from `s` that is actually present in `s`.
s.remove(42)

print()
print("Remove an element from `s` that is actually present in `s`.")
print("s:")
print(s)  # {1, 2, 3}

# (Attempt to) Remove an element from `s` that is actually absent from `s`.
absent_element = 42

print()
print("(Attempt to) Remove an element from `s` that is actually absent from `s`.")

try:
    s.remove(absent_element)
except KeyError:
    print(
        f"    ... we've caught a `KeyErrow`,"
        " b/c {absent_element} is actually absent from `s`"
    )

print("s:")
print(s)  # {1, 2, 3}

# Discard 1 element that is absent from `s` and 1 element that is present in `s`.
s.discard(absent_element)

present_element = 3
s.discard(present_element)

print()
print("Discard 1 element that is absent from `s` and 1 element that is present in `s`.")
print("s:")
print(s)  # {1, 2}

# Check if `s` is a subset of `t`.
t = {1, 2, 7}

print()
print("Check if `s` is a subset of `t`.")
print("t:")
print(t)
print("s <= t:")
print(s <= t)  # True

# Determine the elements in `s` that are not in `t`.
t = {1, 7}

print()
print("Determine the elements in `s` that are not in `t`.")
print("t:")
print(t)
print("s - t:")
print(s - t)  # {2}
