import asyncio
from time import sleep,time
from turtle import st

async def say_after(delay,words):
    await asyncio.sleep(delay)
    print(words)



async def test():
    
    start=time()
    task1=asyncio.create_task(say_after(1,'hello world'))
    task2=asyncio.create_task(say_after(2,'hello python'))    
    mid=time()
    await task1
    await task2
    end=time()
    #使用create_task后，task1和task2并发运行，从耗时结果也可以看到，task1和task2总共耗时2s左右
    print('execute cost %f --- %f'%(mid-start,end-start)) 
    



if __name__ == '__main__':
    asyncio.run(test())

