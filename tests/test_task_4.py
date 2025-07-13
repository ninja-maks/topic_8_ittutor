# STDLIB
import asyncio
import os
import sys

# THIRDPARTY
import aiohttp
import pytest


test_module_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "tasks")
)
if test_module_path not in sys.path:
    sys.path.append(test_module_path)

# FIRSTPARTY
import tasks.task_4 as t4


@pytest.mark.asyncio
async def test_task_semaphor_behavior() -> None:
    max_requests = 10
    count_requests = 50

    async with aiohttp.ClientSession() as session:
        tasks = []
        obj = t4.CacherFileMaker()
        for i in range(count_requests):
            task = asyncio.create_task(obj.fetch(session, i))
            tasks.append(task)
        result = await asyncio.gather(*tasks)
        await asyncio.sleep(3.1)
        assert obj.limiter.semaphore._value == max_requests
        assert len(result) == count_requests
        files_test = [
            file for file in os.listdir(".") if file.endswith(".txt")
        ]
        for i in range(count_requests):
            assert f"test_{i}.txt" in files_test
            os.remove(f"test_{i}.txt")
