# 1. Дано число в диапазоне от 1_000_000 до 20_000_000.
# Получите список простых чисел, которые меньше заданного числа.
# Напишите сначала алгоритм через обычную синхронную реализацию,
# затем используйте для написания многопроцессорную реализация
# данного алгоритма (надо разделить задание на куски
# и дать каждому ядру процессора делать свою часть,
# а затем собрать результат, выясните сколько у вас ядер у процессора,
# можете сделать программу, которая работает с любым числом ядер).
# Запрофилируйте различные реализации алгоритма? Получилось быстрее?

# STDLIB
import multiprocessing

# THIRDPARTY
from line_profiler import LineProfiler
from tqdm import tqdm


def find_simple_sync(num: int = 1000000) -> list[int]:
    if num < 100000 or num >= 20000000:
        raise ValueError("Incorrect value")
    return [i for i in tqdm(range(2, num)) if check_simple(i)]


def check_simple(num: int) -> bool:
    last_possible = num // 2
    for i in range(2, last_possible):
        if num % i == 0:
            return False
    return True


def find_simple_mp(num: int = 1000000) -> list[int]:
    if num < 100000 or num >= 20000000:
        raise ValueError("Incorrect value")
    numbers = [i for i in range(num)]
    results = 0
    with multiprocessing.Pool() as pool:
        results = pool.map(check_simple, numbers)
    return [num for num, is_simple in tqdm(zip(numbers, results)) if is_simple]


def main() -> None:
    lp = LineProfiler(find_simple_sync)
    lp.run("find_simple_sync()")
    lp.print_stats()

    lp = LineProfiler(find_simple_mp)
    lp.run("find_simple_mp()")
    lp.print_stats()


if __name__ == "__main__":
    main()


# 100%|██████████| 999998/999998 [39:29<00:00, 421.99it/s]
# Timer unit: 1e-09 s
#
# Total time: 2369.22 s
# File: /home/updegrab/PycharmProjects/topic_8_ittutor/tasks/task_1.py
# Function: find_simple_sync at line 17
#
# Line #      Hits         Time  Per Hit   % Time  Line Contents
# ==============================================================
#     17                                           def find_simple_sync...
#     18         1        900.0    900.0      0.0      if num < 100000 ...
#     19                                                   raise ValueE...
#     20    999999        2e+12    2e+06    100.0      return [i for i ...
#
# 1000000it [00:01, 890107.30it/s]
# Timer unit: 1e-09 s
#
# Total time: 683.976 s
# File: /home/updegrab/PycharmProjects/topic_8_ittutor/tasks/task_1.py
# Function: find_simple_mp at line 31
#
# Line #      Hits         Time  Per Hit   % Time  Line Contents
# ==============================================================
#     31                                           def find_simple_mp(n...
#     32         1        900.0    900.0      0.0      if num < 100000 ...
#     33                                                   raise ValueE...
#     34   1000001  180485500.0    180.5      0.0      numbers = [i for...
#     35         1        600.0    600.0      0.0      results = 0
#     36         2   38157100.0    2e+07      0.0      with multiproces...
#     37         1        7e+11    7e+11     99.8          results = po...
#     38   1000001  942425899.0    942.4      0.1      return [num for ...
#
#
# Process finished with exit code 0
