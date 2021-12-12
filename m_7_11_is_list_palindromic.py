from m_7_00_common import ListNode, length


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    n = length(L)

    if n == 0:
        return True

    right_it = L
    for _ in range(n // 2 + 1):
        right_it = right_it.next

    for shift_for_left_it in reversed(range(n // 2)):
        left_it = L
        for _ in range(shift_for_left_it):
            left_it = left_it.next

        if left_it.data != right_it.data:
            return False

        right_it = right_it.next

    return True


if __name__ == "__main__":
    # Test: 1/203
    L = None
    r = is_linked_list_a_palindrome(L)
    print(r)  # True (as expected)

    # Test: 3/203
    # fmt: off
    L = ListNode.from_list(
        [2, 5, 3, 1, 3, 5, 3, 4, 2, 5, 5, 6, 3, 2, 2, 4, 3, 4, 5, 6, 6, 5, 4, 3, 4, 2, 2, 3, 6, 5, 5, 2, 4, 3, 5, 3, 1, 3, 5, 2]
    )
    # fmt: on
    r = is_linked_list_a_palindrome(L)
    print(r)  # False (but `True` is expected)
