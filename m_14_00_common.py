class BstNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


if __name__ == "__main__":

    import bintrees

    t = bintrees.RBTree(
        [
            (5, "Alfa"),
            (2, "Bravo"),
            (7, "Charlie"),
            (3, "Delta"),
            (6, "Echo"),
        ]
    )

    print(t[2])  # 'Bravo'

    print(t.min_item())  # (2, 'Bravo')
    print(t.max_item())  # (7, 'Charlie')

    # Docstring:
    # # T.insert(key, value) <==> T[key] = value, insert key, value into tree.
    t.insert(9, "Golf")
    print(
        t
    )  # RBTree({2: 'Bravo', 3: 'Delta', 5: 'Alfa', 6: 'Echo', 7: 'Charlie', 9: 'Golf'})

    t.discard(3)  # RBTree({2: 'Bravo', 5: 'Alfa', 6: 'Echo', 7: 'Charlie', 9: 'Golf'})
    print(t)

    a = t.pop_min()
    print(a)  # (2, 'Bravo')
    print(t)  # RBTree({5: 'Alfa', 6: 'Echo', 7: 'Charlie', 9: 'Golf'})

    b = t.pop_max()
    print(b)  # (9, 'Golf')
    print(t)  # RBTree({5: 'Alfa', 6: 'Echo', 7: 'Charlie'})
