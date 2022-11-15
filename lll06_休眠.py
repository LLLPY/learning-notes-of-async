import asyncio
import datetime


async def say_delay(delay, words):

    # 阻塞delay秒后返回一个打印函数
    say = await asyncio.sleep(delay, print)

    say(words)
    # asyncio.sleep(delay,result=None)
    '''
        1.delay指定阻塞的秒数。
        2.如果指定了result，则当协程完成时将其返回给调用者
        3.sleep()总会挂起当前任务，以允许其他任务执行。
        4.将delay设为0将提供一个经优化的路径以允许其他任务运行。这可供长期间运行的函数以避免
          在函数调用的全程中阻塞事件循环。
    '''

# 程序运行 n s，每秒打印当前日期
async def show_date_in_time(n):
    loop = asyncio.get_running_loop()
    end = loop.time()+n
    while True:
        if loop.time() > end:
            break

        print(datetime.datetime.now())

        await asyncio.sleep(1)


async def test():
    await say_delay(1, 'hello world!')
    await show_date_in_time(5)


if __name__ == '__main__':
    asyncio.run(test())
