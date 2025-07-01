# STDLIB
import asyncio


async def say_hello() -> None:
    await asyncio.sleep(1)
    print("Hello")


async def say_world() -> None:
    await asyncio.sleep(2)
    print("World")


async def main_2() -> None:
    await asyncio.gather(say_hello(), say_world())


asyncio.run(main_2())
