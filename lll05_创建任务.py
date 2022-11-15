import asyncio


async def say_hello():
    print('hello world!')


def done(task):
    print(1111,task)


async def test():
    task=asyncio.create_task(say_hello())
    await task
    #asyncio.create_task(coro,*,name=None)
    '''
         将coro封装成一个Task并调度其执行。
         name：为Task设定名称，同时可以使用Task.set_name()来设定
    
    '''    
    
    task.set_name('say hello!')
    print(task.get_name())
    
    
    
    
    background_tasks=set()
    for i in range(10):
        task=asyncio.create_task(say_hello())
        
        background_tasks.add(task)  
        
        task.add_done_callback(background_tasks.discard)
        # task.add_done_callback(done)
        
        await task #等待task执行完成
        
    
    print(background_tasks)
        



if __name__ == '__main__':
    asyncio.run(test())