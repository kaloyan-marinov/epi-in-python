import timeit


# fmt: off
#
# `timeit.default_timer()` returns
# The default timer, which is always `time.perf_counter()`.
#
# The reference point of the returned value is undefined,
# so that only the difference between the results of two calls is valid.
'''
if __name__ == '__main__':
    start = timeit.default_timer()
    final = timeit.default_timer()

    print(start)
    print(final)
    print(final - start)
'''
# fmt: on


# fmt: off
'''
def time_function(f):
    """
    Print how long a function takes to execute.
    """
    start = timeit.default_timer()

    result = f()

    final = timeit.default_timer()

    print(
        f'Function call took {final - start} seconds to execute.'
    )

    return result


def foo():
    print('I am foo()')


def ackermann(m: int, n: int) -> int:
    """
    Evaluate the Ackermann function.
    """
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(
            m - 1,
            ackermann(m, n - 1),
        )


if __name__ == "__main__":
    # Example 1.
    print()
    time_function(foo)
    
    # Example 2.
    # (
    # `functools.partial` takes a function and positional arguments for it,
    # and creates a new function with those arguments preassigned to the specified values.
    # )
    import functools
    #import sys

    print()

    #print(sys.getrecursionlimit())  # 1000
    #print(sys.setrecursionlimit(2500))
    #print(sys.getrecursionlimit())  # 2500
    
    time_function(
        functools.partial(ackermann, 3, 2),
    )
'''
# fmt: on

def time_function(f):

    def wrapper(*args, **kwargs):
        start = timeit.default_timer()

        result = f(*args, **kwargs)

        final = timeit.default_timer()

        print(
            f'Function call took {final - start} seconds to execute.'
            f' The arguments taken by the function call were {args}\t{kwargs}'
        )

        return result

    return wrapper


@time_function
def foo():
    print('I am foo()')


@time_function
def bar(*args, **kwargs):
    print(sum(args) * sum(kwargs.values()))


@time_function
def ackermann(m: int, n: int) -> int:
    """
    Evaluate the Ackermann function.
    """
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(
            m - 1,
            ackermann(m, n - 1),
        )


if __name__ == '__main__':
    print()
    foo()

    # fmt; off
    print()
    bar(
        1, 2, 3,
        a=10, b=20, c=30,
    )
    # fmt: on

    # The following statement isn't wrong,
    # but, in my view,
    # it prints out too many lines to be useful for this simple demo.
    #print()
    #ackermann(3, 2)
