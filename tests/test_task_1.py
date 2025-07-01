# STDLIB
import os
import sys

# THIRDPARTY
import pytest


test_module_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "tasks")
)
if test_module_path not in sys.path:
    sys.path.append(test_module_path)

# FIRSTPARTY
import tasks.task_1 as t1


@pytest.mark.parametrize(
    "n, expected",
    [
        (10, [2, 3, 5, 7]),
        (2, []),
        (20, [2, 3, 5, 7, 11, 13, 17, 19]),
        (1, []),
        (0, []),
        (-10, []),
        (9, [2, 3, 5, 7]),
    ],
)
def test_task_1_sync(n: int, expected: list[int]) -> None:
    assert t1.find_simple_sync(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (10, [2, 3, 5, 7]),
        (2, []),
        (20, [2, 3, 5, 7, 11, 13, 17, 19]),
        (1, []),
        (0, []),
        (-10, []),
        (9, [2, 3, 5, 7]),
    ],
)
def test_task_mp(n: int, expected: list[int]) -> None:
    assert t1.find_simple_mp(n) == expected
