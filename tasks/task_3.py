# 3. Реализуйте асинхронный метод,
# который будет отправлять запросы в [http://google.com]
# (http://google.com "smart-link") по http
# с ограничением не более 10 запросов в единицу времени.

# STDLIB
import asyncio

# THIRDPARTY
import aiohttp


MAX_REQUESTS = 10
semaphore = asyncio.Semaphore(MAX_REQUESTS)


async def task_semaphor() -> None:
    while True:
        await asyncio.sleep(1)
        for _ in range(MAX_REQUESTS - semaphore._value):
            semaphore.release()


async def fetch(session: aiohttp.ClientSession, i: int) -> None:
    async with semaphore:
        async with session.get("http://google.com") as response:
            # await asyncio.sleep(5)
            print(f"{i} - {response}")


async def main() -> None:
    async with aiohttp.ClientSession() as session:
        asyncio.create_task(task_semaphor())
        tasks = []
        for i in range(30):
            task = asyncio.create_task(fetch(session, i))
            tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
    # list_i = [1,2,3,4]
    # print(list_i)
