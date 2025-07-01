# STDLIB
import asyncio


async def get_data() -> str:
    await asyncio.sleep(1)
    return "data"


async def process_data() -> None:
    data = await get_data()
    print(f"Processing {data}")


async def main() -> None:
    tasks = [process_data() for _ in range(5)]
    await asyncio.gather(*tasks)


asyncio.run(main())
