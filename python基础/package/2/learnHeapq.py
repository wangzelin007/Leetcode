# _*_ coding: utf-8 _*_
# 堆是一个二叉树,满足父节点小于或大于孩子节点
# heap[k] <= heap[2*k+1] 和 heap[k] <= heap[2*k+2] 小根堆
# heap[k] >= heap[2*k+1] 和 heap[k] >= heap[2*k+2] 大根堆
# 将 item 的值加入 heap 中，保持堆的不变性。
# heapq.heappush(heap, item)
# 弹出并返回 heap 的最小的元素，保持堆的不变性。如果堆为空，抛出 IndexError 。
# heapq.heappop(heap)
# 只访问最小的元素 可以把堆看成原生的 python list
# heap[0]
# 将 item 放入堆中，然后弹出并返回 heap 的最小元素。
# heapq.heappushpop(heap, item)
# 将list x 转换成堆，原地，线性时间内。
# heapq.heapify(x)
# 弹出并返回 heap 中最小的一项，同时推入新的 item。
# 堆的大小不变。 如果堆为空则引发 IndexError。
# 和 heappushpop 区别在于返回的值有可能比 item 更大
# heapq.heapreplace(heap, item)
# 类似于 sorted(itertools.chain(*iterables))
# 将多个已排序的输入合并为一个已排序的输出
# heapq.merge(*iterables)
# heapq.nlargest(n, iterable[, key])
# heapq.nsmallest(n, iterable[, key])

from heapq import *
h = []
heappush(h, (5, 'write code'))
heappush(h, (7, 'release product'))
heappush(h, (1, 'write spec'))
heappush(h, (3, 'create tests'))
heappop(h) #(1, 'write spec')

# 堆常用于实现优先队列 todo
import itertools
pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')
