# Define a stack:
s = [1, 2, 3]

print()
print("s")
print(s)

# Push an element on to `s`:
e = 4
s.append(e)

print()
print("s")
print(s)

# Retrieve the element at the top of `s` _without_ removing it:
top = s[-1]

print()
print("top")
print(top)
print("s")
print(s)

# Remove and return the element at the top of `s`:
top = s.pop()

print()
print("top")
print(top)
print("s")
print(s)

# Test if `s` is empty.
is_empty = len(s) == 0

print()
print("is_empty")
print(is_empty)
