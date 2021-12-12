from m_7_00_common import ListNode, length


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    n = length(L)

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

    # When the next statement is executed, the script crashes with
    #   ```
    #     File "m_7_11_is_list_palindromic.py", line 9, in is_linked_list_a_palindrome
    #       right_it = right_it.next
    #   AttributeError: 'NoneType' object has no attribute 'next'
    #   ```
    r = is_linked_list_a_palindrome(L)
    print(r)
