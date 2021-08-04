from typing import List, Set


def max_guests_in_time(guest_timelines: List[Set]):
    tmp = {}
    max_val = 0
    count = 0
    for i in guest_timelines:
        tmp[i[0]] = tmp.get(i[0], 0) + 1
        tmp[i[1]] = tmp.get(i[1], 0) - 1

    for _, j in sorted(tmp.items()):
        count += j
        max_val = count if count >= max_val else max_val
    return max_val


assert (
    max_guests_in_time([(1, 7), (1, 4), (7, 8), (3, 4), (5, 11), (3, 9)]) == 4
), "Should be 4"
assert max_guests_in_time([(1, 7), (1, 4)]) == 2, "Should be 2"
assert max_guests_in_time([(5, 7), (1, 4)]) == 1, "Should be 1"
