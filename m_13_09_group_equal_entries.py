from typing import List

import collections

Person = collections.namedtuple(
    "Person",
    ("age", "name"),
)


def group_by_age_1(people: List[Person]) -> None:

    age_2_count = collections.Counter((person.age for person in people))

    ii = 0
    while ii < len(people):
        people_ii = people[ii]
        count = age_2_count[people_ii.age]

        count -= 1

        write_idx = ii + 1
        jj = ii + 1
        while count > 0:
            if people[jj].age == people_ii.age:
                people[write_idx], people[jj] = people[jj], people[write_idx]
                write_idx += 1
                count -= 1
            jj += 1

        ii = write_idx

    return


def group_by_age(people: List[Person]) -> None:

    # For each distinct age, determine a subarray,
    # which at the end of the function will hold all `Person`s of the same age.
    # (Specify each such subarray by its start index and size.)
    age_2_count = collections.Counter((person.age for person in people))

    age_2_offset = {}
    offset = 0
    for age, count in age_2_count.items():
        age_2_offset[age] = offset
        offset += count

    # Consider each of the determined subarrays as
    # a subarray, each of whose elements will be processed individually.
    # After processing an element from a given subarray,
    # we account for that by "decreasing the subarray's length by 1".
    while age_2_offset:
        from_age = next(iter(age_2_offset))
        from_idx = age_2_offset[from_age]

        to_age = people[from_idx].age
        to_idx = age_2_offset[people[from_idx].age]  # or simply `age_2_offset[to_age]`

        people[from_idx], people[to_idx] = people[to_idx], people[from_idx]

        # "Decrease the subarray's length by 1."
        age_2_count[to_age] -= 1
        if age_2_count[to_age] > 0:
            age_2_offset[to_age] = to_idx + 1
        else:
            del age_2_offset[to_age]
