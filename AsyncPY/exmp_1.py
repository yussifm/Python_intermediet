import asyncio

async def main():
    await asyncio.sleep(delay=1.0)
    task1 = asyncio.create_task(coro= foofunc())
    value = await task1
    print("hello")
 
  
    
    
async def foofunc():
    await asyncio.sleep(delay=2.0)
    print("second foo func")   
    
    
asyncio.run(main=main())
