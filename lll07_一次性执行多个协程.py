import asyncio
import time


#计算阶层
async def factorial(name, number):
    f = 1
    for i in range(2, number+1):
        print(f'Task {name}: Compute factorial({number}), curiently i={i}...')
        await asyncio.sleep(1)
        f *= i/0
    print(f'Task {name}: factorial({number})={f}')
    return f


async def main():
    
    start=time.time()
    L = await asyncio.gather(
        factorial('A', 2),
        factorial('B', 3),
        factorial('C', 4),
        factorial('D', 5),
        return_exceptions=True
    )
    
    '''
    asyncio.gather(*aws,return_exceptions=False)
        传入的所有coroutine会被自动的调度为Task，并发的运行aws中的coroutine
        aws:coroutine序列
        
        返回值：
            如果所有的coroutine都执行完成并没有报错，则返回一个列表，列表中每一个值对应aws中每一个coroutine的返回值（顺序保持不变）
            
            如果return_exceptions值为False，则序列中的某一个任务执行失败，其他的任务不会被取消
            如果return_exceptions值为True，则异常会被当作成功的返回结果
        
        如果gather()被取消，则它下面的所有任务也会被取消
        序列中的任意任务被取消不后影响其他任务的执行
    '''
    end=time.time()
    print(f'costs {end-start} s')
    print(L)


if __name__ == '__main__':
    asyncio.run(main())
