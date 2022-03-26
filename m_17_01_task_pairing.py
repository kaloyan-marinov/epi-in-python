import collections
from typing import List

PairedTasks = collections.namedtuple(
    "PairedTasks",
    ("task_1", "task_2"),
)


def optimum_task_assignment(
    task_durations: List[int],
) -> List[PairedTasks]:
    """
    Assume that `len(task_durations)` is even.
    """
    n = len(task_durations)

    task_id_pairs = [(t_d_i, i) for i, t_d_i in enumerate(task_durations)]
    task_id_pairs.sort(key=lambda pair: pair[0])

    """
    return [PairedTasks(task_1=idx, task_2=n - 1 - idx) for idx in range(n // 2)]
    """
    return [
        PairedTasks(task_1=task_id_pairs[idx][0], task_2=task_id_pairs[n - 1 - idx][0])
        for idx in range(n // 2)
    ]


def optimum_task_assignment_2(
    task_durations: List[int],
) -> List[PairedTasks]:
    """
    Assume that `len(task_durations)` is even.
    """

    task_durations.sort()

    return [
        PairedTasks(
            task_1=task_durations[i],
            task_2=task_durations[~i],
        )
        for i in range(len(task_durations) // 2)
    ]
