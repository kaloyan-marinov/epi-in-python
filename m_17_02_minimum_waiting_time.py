from typing import List


def minimum_total_waiting_time(service_times: List[int]) -> int:
    service_times.sort()

    total = 0
    curr = 0
    for s_t in service_times[:-1]:
        curr += s_t
        total += curr

    return total


def minimum_total_waiting_time_2(service_times: List[int]) -> int:
    service_times.sort()

    total_waiting_time = 0
    for i, s_t_i in enumerate(service_times):
        num_remaining_queries = len(service_times) - (i + 1)
        total_waiting_time += num_remaining_queries * s_t_i

    return total_waiting_time
