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

# FIRSTPARTY
import tasks.task_2 as t2


@pytest.mark.parametrize(
    "n",
    [
        10,
        2,
        20,
        1,
        0,
        9,
    ],
)
def test_task_2_possitive(n: int) -> None:
    files_folder = os.path.join(os.path.dirname(__file__), "tmp")
    os.makedirs(name=files_folder, exist_ok=True)
    t2.mp_file_maker(files_folder, n)
    res = os.listdir(files_folder)
    for _ in res:
        with open(os.path.join(files_folder, _), "r") as file:
            assert _ == f"file_{file.readlines()[0]}.txt"
    [
        os.remove(os.path.join(files_folder, _))
        for _ in res
        if _.endswith(".txt")
    ]
    os.rmdir(files_folder)
    assert len(res) == n


@pytest.mark.parametrize(
    "n",
    [
        -10,
        -9,
    ],
)
def test_task_2_negative(n: int) -> None:
    files_folder = os.path.join(os.path.dirname(__file__), "tmp")
    os.makedirs(name=files_folder, exist_ok=True)
    with pytest.raises(ValueError):
        t2.mp_file_maker(files_folder, n)
    os.rmdir(files_folder)
