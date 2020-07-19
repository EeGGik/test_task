import pytest
from task_one import time_delta_specifier


# Correctness tests
@pytest.mark.parametrize("time, result", [("30", 30),
                                          ("30s", 30),
                                          ('s', 1),
                                          ('60.5m', 3630)])
def test_time_delta_specifier(time, result):
    test = time_delta_specifier(time)
    assert (test == result)


# Rises exception tests
@pytest.mark.parametrize("time", ["",
                                  "10seconds",
                                  "1m30s",
                                  "1y",
                                  "s12m",
                                  "asdasda"])
def test_time_delta_specifier_exceptions(time):
    with pytest.raises(ValueError):
        time_delta_specifier(time)
