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
import typing as types

# THIRDPARTY
import aiohttp
from async_limiter import DualRateLimiter


class CacherFileMaker:

    def __init__(self: types.Self) -> None:
        self.limiter = DualRateLimiter(
            max_concurrent=10,
            max_requests=10,
            time_period=1,
            name="some_class",
        )

    async def fetch(
        self: types.Self, session: aiohttp.ClientSession, i: int
    ) -> None:
        async with self.limiter:
            async with session.get("https://example.com") as response:
                print(1)
                with open(f"test_{i}.txt", "a+") as file:
                    file.write(str(response.status))


async def main() -> None:
    async with aiohttp.ClientSession() as session:
        obj = CacherFileMaker()
        tasks = []
        for i in range(50):
            task = asyncio.create_task(obj.fetch(session, i))
            tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
