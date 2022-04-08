import asyncio
import time

from async_demos.web.tasks import slow_task


async def shopper1():
    # time.sleep(1)
    print('--- Worker 1: Start')
    await asyncio.sleep(5)
    print('--- Worker 1: End')
    return 'bread'


async def shopper2():
    # time.sleep(2)
    print('--- Worker 2: Start')
    await asyncio.sleep(2)
    print('--- Worker 2: End')
    return 'cheese'


async def shopper3():
    # time.sleep(3)
    print('--- Worker 3: Start')
    await asyncio.sleep(5)
    print('--- Worker 3: End')

    return 'bacon'


def cook(ingredients):
    print(f'Making sandwich with {ingredients}')


async def main():
    start = time.time()

    sandwich_parts = await asyncio.gather(
        shopper1(),  # 1
        shopper2(),  # 2
        shopper3(),  # 3
    )
    # sync  => total = 1 + 2 + 3 = 6
    # async => total = max(1, 2, 3) = 3

    cook(sandwich_parts)

    end = time.time()

    print(f'Executed in {end - start} s')


# main()
# asyncio.run(main())

# slow_task(5)
