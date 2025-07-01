# STDLIB
import asyncio


async def main_1() -> None:
    print("Hello")
    await asyncio.sleep(1)
    print("World")


asyncio.run(main_1())
