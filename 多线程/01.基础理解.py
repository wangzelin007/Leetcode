# coding:utf-8
import threading
import time

def get_list_page():
    print("列表页抓取开始\n")
    time.sleep(3)
    print("列表页抓取结束\n")

def get_detail_page():
    print("详情页抓取开始\n")
    time.sleep(2)
    print("详情页抓取结束\n")

# 创建两个子线程
thread1 = threading.Thread(target=get_list_page)
thread2 = threading.Thread(target=get_detail_page)
start_time = time.time()
# # 设置线程守护
thread1.setDaemon(True)
thread2.setDaemon(True)
# 启动两个线程
thread1.start()
thread2.start()
# # 设置线程阻塞
thread1.join()
thread2.join()
print("Run time is {}".format(time.time() - start_time))

# 1. 只有t.start()时
# 解释：三个线程基本属于并发，主线程、子线程1、子线程2会同时运行，各干各的，并且，主线程会等到两个子线程结束后，才会结束。
# 列表页抓取开始
# 详情页抓取开始
# Run time is 0.00025010108947753906
# 详情页抓取结束
# 列表页抓取结束

# 2. 增加t.setDeamon 时
# 解释：有了守护线程之后，主线程就会在自身结束后，（不管守护线程还是不是在运行）kill掉守护线程。
# 列表页抓取开始
# 详情页抓取开始
# Run time is 0.00024390220642089844

# 3. 增加t.join 时
# 解释：有了线程阻塞后，主线程就会停在join那里，等待阻塞的子线程运行结束，然后再继续执行。
# 列表页抓取开始
# 详情页抓取开始
# 详情页抓取结束
# 列表页抓取结束
# Run time is 3.0005598068237305

# join 用于阻塞主线程，可以想象成将某个子线程的执行过程插入(join)到主线程的时间线上，
# 主线程的后续代码延后执行，主线程会停在join那里，等待阻塞的子线程运行结束，然后再继续执行。
# 注意和 t.start() 分开写在两个for循环中。
# 第一个for循环同时启动了所有子线程，
# 随后在第二个for循环中执行t.join() ，
# 主线程实际被阻塞的总时长==其中执行时间最长的一个子线程。