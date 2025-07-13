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
import tasks.task_3 as t3


@pytest.mark.asyncio
async def test_task_semaphor_behavior_min() -> None:
    max_requests = 10
    count_requests = 30

    async with aiohttp.ClientSession() as session:
        tasks = []
        obj = t3.Requester()
        for i in range(count_requests):
            task = asyncio.create_task(obj.fetch(session, i))
            tasks.append(task)
        result = await asyncio.gather(*tasks)
        await asyncio.sleep(3.1)
        assert obj.limiter.semaphore._value == max_requests
        assert len(result) == count_requests


@pytest.mark.asyncio
async def test_task_semaphor_behavior_max_1() -> None:
    max_requests = 10
    count_requests = 30

    async with aiohttp.ClientSession() as session:
        tasks = []
        obj = t3.Requester()
        for i in range(count_requests):
            task = asyncio.create_task(obj.fetch(session, i))
            tasks.append(task)
        result = await asyncio.gather(*tasks)
        await asyncio.sleep(0.9)
        assert obj.limiter.semaphore._value == max_requests
        assert len(result) == count_requests


@pytest.mark.asyncio
async def test_task_semaphor_behavior_max_2() -> None:
    max_requests = 10
    count_requests = 30

    async with aiohttp.ClientSession() as session:
        tasks = []
        obj = t3.Requester()
        for i in range(count_requests):
            task = asyncio.create_task(obj.fetch(session, i))
            tasks.append(task)
        result = await asyncio.gather(*tasks)
        await asyncio.sleep(0.2)
        assert obj.limiter.semaphore._value == max_requests
        assert len(result) == count_requests


@pytest.mark.asyncio
async def test_task_semaphor_behavior_max_3() -> None:
    max_requests = 10
    count_requests = 30

    async with aiohttp.ClientSession() as session:
        tasks = []
        count_requests = 30
        obj = t3.Requester()
        for i in range(count_requests):
            task = asyncio.create_task(obj.fetch(session, i))
            tasks.append(task)
        result = await asyncio.gather(*tasks)
        await asyncio.sleep(0.1)
        assert obj.limiter.semaphore._value == max_requests
        assert len(result) == count_requests
