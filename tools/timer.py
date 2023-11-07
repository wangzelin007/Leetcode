import time

# 定义一个装饰器函数，用于统计函数的运行时间
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # 记录函数开始时间
        result = func(*args, **kwargs)  # 执行原始函数
        end_time = time.time()  # 记录函数结束时间
        elapsed_time = end_time - start_time  # 计算函数运行时间
        print(f"{func.__name__} 运行时间: {elapsed_time} 秒")
        return result
    return wrapper

# 使用装饰器来装饰需要统计运行时间的函数
@timing_decorator
def some_function():
    # 模拟一些耗时操作
    time.sleep(2)
    print("Function executed.")

@timing_decorator
def another_function():
    # 模拟一些耗时操作
    time.sleep(1)
    print("Another function executed.")

# 调用装饰后的函数
some_function()
another_function()
