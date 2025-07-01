# STDLIB
import asyncio

# THIRDPARTY
import aiohttp


async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main() -> None:
    urls = ["http://google.com", "http://yandex.ru"]
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)


asyncio.run(main())
