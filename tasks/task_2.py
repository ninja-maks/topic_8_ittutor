# 2. Напишите скрипт который создаст параллельно
# 10 файлов с именем `file_{index}.txt'
# и записывает их номер внутрь файла.
# STDLIB
import multiprocessing


def make_file(file_name: str, to_contain: str) -> None:
    with open(file_name, "a+") as file:
        file.write(to_contain)


def mp_file_maker(path_file: str, file_num: int) -> None:
    if file_num < 0:
        raise ValueError("Incorrect file_num!")
    args = [
        (f"{path_file}/file_{str(i)}.txt", str(i)) for i in range(file_num)
    ]
    with multiprocessing.Pool() as pool:
        pool.starmap(make_file, args)


if __name__ == "__main__":
    mp_file_maker(".", 10)
