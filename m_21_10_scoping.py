x = "global-x"
y = "global-y"
z = "global-z"


def basic_scoping():
    print(x)
    y = "local-y"
    global z
    z = "local-z"


print()

basic_scoping()  # global-x

print(x)  # global-x
print(y)  # global-y
print(z)  # local-z


def inner_outer_scoping():
    def inner_1():
        print(x)

    def inner_2():
        x = "inner_2-x"
        print(x)

    def inner_3():
        nonlocal x
        x = "inner_3-x"
        print(x)

    x = "outer-x"

    inner_1()
    inner_2()
    inner_3()

    print(x)


print()

inner_outer_scoping()
# fmt: off
'''
outer-x
inner_2-x
inner_3-x
inner_3-x
'''
# fmt: on

print(x)  # global-x
print(y)  # global-y
print(z)  # local-z


def outer_scope_error():
    def inner():
        try:
            x = x + 1
        except NameError:
            print("Error: `x` is local, so `x + 1` is not defined yet")

    x = 123
    inner()


print()

outer_scope_error()  # Error: `x` is local, so `x + 1` is not defined yet


def outer_scope_no_error():
    def inner():
        x[0] = -x[
            0
        ]  # `x[0]` isn't a variable[/symbol, so it] gets resolved from the outer `x`

    x = [314]
    inner()
    print(x[0], x)


print()

outer_scope_no_error()  # -314 [-314]
