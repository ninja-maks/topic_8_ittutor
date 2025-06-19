# 4. Написать асинхронный код,
# который делает 50 get запросов
# к [https://example.com/]
# (https://example.com/ "smart-link").
# Записать все статусы ответов в файл
# и убедиться, что количество запросов
# соответствует заданному количеству.
# Необходимо учесть, чтобы одновременно
# выполнялось не больше 10 запросов.
# Для выполнения запросов использовать библиотеку aiohttp.
# Все значения, количество запросов,
# лимит одновременно выполняемых запросов
# и url должны передаваться как параметры.

# STDLIB
import asyncio

# THIRDPARTY
import aiohttp


MAX_REQUESTS = 10
semaphore = asyncio.Semaphore(MAX_REQUESTS)


async def func_semaphore() -> None:
    while True:
        await asyncio.sleep(1)
        for _ in range(MAX_REQUESTS - semaphore._value):
            semaphore.release()


async def fetch(session: aiohttp.ClientSession, i: int) -> None:
    async with semaphore:
        async with session.get("https://example.com") as response:
            with open(f"test_{i}.txt", "a+") as file:
                file.write(str(response.status))


async def main() -> None:
    async with aiohttp.ClientSession() as session:
        asyncio.create_task(func_semaphore())

        tasks = []
        for i in range(50):
            task = asyncio.create_task(fetch(session, i))
            tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
