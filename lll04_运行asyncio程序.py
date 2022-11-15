import asyncio




async def say_hello():
    print('hello python!')
    


async def test():
    await say_hello()
    
    #下面这条语句会执行失败，因为在一个asyncio事件循环内部不能有其他的asyncio事件循环
    # asyncio.run(say_hello())
    
    return 'coroutine done!'

    
if  __name__ == '__main__':


    #asyncio.run(coro,*,debug=False)  
    '''
        1.执行coroutine coro并返回结果
        2.run函数会执行传入的协程，负责管理asyncio事件循环，终结异步生成器，关闭线程池等。
        3.当有其他的asyncio事件循环在同一个线程中运行时，不能调用它。
        4.如果debug=True，将以调试模式运行
        5.run函数总是会创建一个新的事件循环并在结束的时候关闭它，它应当被当作asyncio程序的主入口点，理想情况下应当只被调用一次
    
    '''

    
    res=asyncio.run(test())
    print(res)






