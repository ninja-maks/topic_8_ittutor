# 2. Напишите скрипт который создаст параллельно
# 10 файлов с именем `file_{index}.txt'
# и записывает их номер внутрь файла.
# STDLIB
import multiprocessing


def make_file(file_name: str) -> None:
    with open(file_name, "a+") as file:
        file.write(file_name.split("_")[1].split(".")[0])


if __name__ == "__main__":
    args = [f"file_{str(i)}.txt" for i in range(10)]
    with multiprocessing.Pool() as pool:
        results = pool.map(make_file, args)
