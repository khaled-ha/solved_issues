import asyncio
import time

async def async_sleep(n):
    print('before sleep',n)
    try:
        for i in range(n):
            yield i
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        pass
    print('after sleep',n)

async def return_hello():
    print('hello')

async def main():
    async for i in async_sleep(5):
        print(i)
    start = time.time()
    # task = asyncio.create_task(async_sleep(1))
    # await async_sleep(2)
    # await task
    # res =  await return_hello()
    # print(res)
    # asyncio.gather(async_sleep(2), async_sleep(1), return_hello())
    print('finished at ',time.time() - start)

if __name__ == '__main__':
    asyncio.run(main())