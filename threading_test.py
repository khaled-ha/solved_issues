import asyncio 
import time

async def main():
    print(f'{time.ctime()} hello')
    await asyncio.sleep(1.0)
    print(f'{time.ctime()} goodbye')

asyncio.run(main())