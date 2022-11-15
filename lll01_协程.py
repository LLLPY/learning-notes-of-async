import asyncio
import time
    

async def say_afeter(delay,msg):
    await asyncio.sleep(delay)
    print(msg)



async def test():
    start=time.time()    
    await say_afeter(1,'hello world')
    await say_afeter(2,'hello python')
    end =time.time()
    print('execute cost %f'%(end- start))


if __name__=="__main__":
    asyncio.run(test()) 