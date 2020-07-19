import pytest
from task_three import merge_gen
from heapq import merge


# Correctness tests
@pytest.mark.parametrize("itterable", [([1, 5, 9], [2, 5], [1, 6, 10, 11]),
                                       ([1, 2], [1, 2, 3]),
                                       ([5, 6], [i for i in range(50)])
                                       ])
def test_time_delta_specifier(itterable):
    test = list(merge(*itterable))
    print(test)
    result = list(merge_gen(*itterable))
    print(result)
    assert (test == result)