import heapq


min_heap = [
    (5, "write code"),
    (7, "release product"),
    (1, "write specs"),
]

# Perform an in-place transformation
# of the `min_heap` list
# into a heap data structure,
# in linear time.
heapq.heapify(min_heap)

print()
print("type(min_heap):")
print(type(min_heap))

# Return a list with the `n` smallest elements
# from the dataset defined by the 2nd parameter.
# (
#   The 2nd parameter need not be a "heapified list";
#   more generally, it may be a Python iterable.
# )
n = 2
top_2 = heapq.nsmallest(n, min_heap)

print()
print("top_2:")
print(top_2)  # [(1, 'write specs'), (5, 'write code')]

# Push a new item onto the heap.
new_item = (3, "create tests")

heapq.heappush(min_heap, new_item)

top_2 = heapq.nsmallest(n, min_heap)

print()
print(f"Push {new_item} as a new item onto the heap...")
print("top_2:")
print(top_2)  # [(1, 'write specs'), (3, 'create tests')]

# Access the smallest item without popping it.
print()
print("Access the smallest item without popping it...")
print("min_heap[0]")
print(min_heap[0])

top_2 = heapq.nsmallest(n, min_heap)
print("top_2:")
print(top_2)  # [(1, 'write specs'), (3, 'create tests')]

# Pop and return the smallest item.
smallest_item = heapq.heappop(min_heap)

print()
print("Pop and return the smallest item...")
print("smallest_item:")
print(smallest_item)  # (1, 'write specs')

top_2 = heapq.nsmallest(n, min_heap)
print("top_2:")
print(top_2)  # [(3, 'create tests'), (5, 'write code')]

# Push a new item onto the heap, then pop and return the smallest item.
new_item = (9, "analyse release in a retrospective")

smallest_item = heapq.heappushpop(min_heap, new_item)

print()
print("Push a new item onto the heap, then pop and return the smallest item...")
print("smallest_item:")
print(smallest_item)  # (3, 'create tests')

top_2 = heapq.nsmallest(n, min_heap)
print("top_2:")
print(top_2)  # [(5, 'write code'), (7, 'release product')]

print("min_heap:")
print(
    min_heap
)  # [(5, 'write code'), (7, 'release product'), (9, 'analyse release in a retrospective')]
