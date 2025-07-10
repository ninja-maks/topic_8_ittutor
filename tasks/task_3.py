# 3. Реализуйте асинхронный метод,
# который будет отправлять запросы в [http://google.com]
# (http://google.com "smart-link") по http
# с ограничением не более 10 запросов в единицу времени.

# STDLIB
import asyncio
import typing as types

# THIRDPARTY
import aiohttp
from async_limiter import DualRateLimiter


class Requester:

    def __init__(
        self: types.Self, base_url: str = "https://google.com"
    ) -> None:
        self.url = base_url
        self.limiter = DualRateLimiter(
            max_concurrent=10, max_requests=10, time_period=1, name=base_url
        )

    async def fetch(
        self: types.Self, session: aiohttp.ClientSession, i: int
    ) -> str:
        async with self.limiter:
            async with session.get(self.url) as response:
                return f"{i} - {response}"


async def main() -> list:
    async with aiohttp.ClientSession() as session:
        obj = Requester()
        tasks = []
        for i in range(30):
            task = asyncio.create_task(obj.fetch(session, i))
            tasks.append(task)
        return await asyncio.gather(*tasks)


if __name__ == "__main__":
    print(asyncio.run(main()))
    # list_i = [1,2,3,4]
    # print(list_i)
