# STDLIB
import asyncio
from typing import Any, AsyncGenerator


async def async_generator() -> AsyncGenerator[int, Any]:
    for i in range(3):
        await asyncio.sleep(1)
        yield i


async def main() -> None:
    async for i in async_generator():
        print(i)


asyncio.run(main())
