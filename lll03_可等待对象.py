import asyncio
from operator import ne



#可等待对象
'''
如果一个对象可以在await语句中使用，那么它就是可等待对象。
可等待的对象有三种类型：
    1.协程
    2.任务
    3.Future


#协程
    1.协程函数：使用async定义的函数被称为协程函数
    2.协程对象：协程函数返回的对象就是协程对象

#任务
    通过asyncio.create_task(async fun)可以将一个协程函数func转成一个任务，任务会被自动调度执行

#Future
    1.Future是一种特殊的低层级可等待对象，表示一个异步操作的最终结果。
    2.当一个Future对象被等待，这意味着协程将保持等待直到该Future对象在其他地方的操作完毕。
    3.通常情况下，没有必要在应用层面创建Future对象



'''



#协程
async def nested():
    for i in  range(10):
        print('hello python!')
    return 200



async def test():
    
    
    #协程
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    nested() #仅仅调用协程函数，而不使用await关键字，它是不会被执行的
    
    print(await nested())
    
    
    
    #task
    '''
    通过create_task将协程函数封装成任务后，它会被自动调度执行
    '''
    task=asyncio.create_task(nested())
    print(type(task),task)
    #在这里可以取消任务
    # task.cancel()
    
    
    
    await task #可以使用await关键字等待任务被执行完成后再继后面的任务
    
    print('task之后的代码被执行了！！！！')
    
    
    
    

if __name__ == '__main__':
    asyncio.run(test())