# 请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
# 若队列为空，pop_front 和 max_value需要返回 -1
# 示例 1：
# 输入:
# ["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
# [[],[1],[2],[],[],[]]
# 输出:[null,null,null,2,1,2]
# 示例 2：
# 输入:
# ["MaxQueue","pop_front","max_value"]
# [[],[],[]]
# 输出:[null,-1,-1]
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# class MaxQueue1:
#
#     def __init__(self):
#         self.q = []
#         self.max = []
#
#     def max_value(self) -> int:
#         return self.max[0] if self.max else -1
#
#     def push_back(self, value: int) -> None:
#         while self.max and value > self.max[-1]:
#             self.max.pop()
#         self.q.append(value)
#         self.max.append(value) # [3, 1] or [4]
#
#     def pop_front(self) -> int:
#         if self.max:
#             res = self.q.pop(0)
#             if res == self.max[0]:
#                 self.max.pop(0)
#             return res
#         else:
#             return -1

# 优化直接使用deque
# from collections import deque
import queue
class MaxQueue2:
    def __init__(self):
        self.q = queue.Queue()
        self.max = queue.deque()

    def max_value(self) -> int:
        return self.max[0] if self.max else -1

    def push_back(self, value: int) -> None:
        self.q.put(value)
        while self.max and value > self.max[-1]:
            self.max.pop()
        self.max.append(value)

    def pop_front(self) -> int:
        if self.q.empty(): return -1
        val = self.q.get()
        if val == self.max[0]:
            self.max.popleft()
        return val

if __name__ == '__main__':
    obj = MaxQueue2()
    # 1
    # print(obj.push_back(1))
    # print(obj.push_back(2))
    # print(obj.max_value())
    # print(obj.pop_front())
    # print(obj.max_value())
    # 2
    print(obj.pop_front())
    print(obj.pop_front())
    print(obj.pop_front())
    print(obj.pop_front())
    print(obj.pop_front())
    print(obj.push_back(15))
    print(obj.max_value())
    print(obj.push_back(9))
    print(obj.max_value())
