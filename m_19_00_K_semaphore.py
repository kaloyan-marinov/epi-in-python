import threading


class Semaphore:
    """
    This models a (powerful) synchronization construct called a "semaphore".

    Conceptually, this construct maintains a set of permits:

        - a thread calling `acquire()` [on a semaphore instance]
          waits, if necessary, until a permit is available,
          and then takes it;

        - a thread calling `release()` [on a semaphore instance]
          adds a permit
          and notifies threads waiting on that semaphore,
          potentially releasing a blocked acquirer.

    ------------------------------

    [ from https://docs.python.org/3/library/threading.html ]

        This is one of the oldest synchronization primitives
        in the history of computer science,
        invented by the early Dutch computer scientist Edsger W. Dijkstra...

        A semaphore manages an internal counter which is
        decremented by each `acquire()` call and
        incremented by each `release()` call.
        The counter [is] never [allowed (by the semaphore's logic itself!) to] go below zero;
        when `acquire()` finds that [the counter] is zero,
        it blocks, waiting until some other thread calls `release()`.



        A `BoundedSemaphore` checks to make sure
        its current value doesn’t exceed its initial value.

        In most situations semaphores are used to guard resources with limited capacity.

        If the semaphore is released too many times it’s a sign of a bug.



        [Bounded]Semaphore Example

        Semaphores are often used to guard resources with limited capacity,
        for example, a database server.
        In any situation where the size[/capacity] of the resource is fixed,
        you should use a [`BoundedSemaphore`].

        Before spawning _any worker threads_,
        _your main thread_ [should] initialize [a `BoundedSemaphore`]:
        ```
        max_connections = 5
        # ...
        pool_bounded_semaphore = BoundedSemaphore(value=max_connections)
        ```

        Once spawned,
        _worker threads_ call the [bounded] semaphore’s `acquire` and `release` methods
        when they need to connect to the [database] server:
        ```
        with pool_bounded_semaphore:
            conn = connect_to_db()
            try:
                # ... use the `conn` ...
            finally:
                conn.close()
        ```

        The use of a [`BoundedSemaphore`] reduces the chance
        that a programming error[,]
        which causes the semaphore to be released more [times] than it’s acquired[,]
        will go undetected.
    """

    def __init__(self, max_available):
        self.cv = threading.Condition()
        self.MAX_AVAILABLE = max_available
        self.taken = 0

    def acquire(self):
        self.cv.acquire()

        while self.taken == self.MAX_AVAILABLE:
            self.cv.wait()
        self.taken += 1

        self.cv.release()

    def release(self):
        self.cv.acquire()

        self.taken -= 1
        self.cv.notify()

        self.cv.release()
