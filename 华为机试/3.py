# coding: utf-8
# 输入描述：
# 输入的第一行为每位面试官的最多面试人次m，第二行为当天总的面试场数n，
# 接下来的n行为每场面试的起始时间和结束时间，起始时间和结束时间用空格分隔
# 其中1<=n,m<=500
# 输出描述：输出一个整数，表示至少需要的面试官数量。
# 例1：输入：
# 3
# 3
# 8 35
# 5 10
# 1 3
# 输出：
# 2

# 例2：输入：
# 2
# 6
# 0 5
# 6 8
# 0 2
# 4 5
# 1 7
# 6 10
# 输出：
# 4
# 说明：本题难点是每位面试官有最多面试人次限制。
# 作者：凸
# 链接：https://leetcode-cn.com/circle/discuss/lmSvYS/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 1. 二分查找算法，最少面试官人数直接定为n // m，最大面试官人数为面试场次数n；
# 2. 定义一个小顶堆p_free和一个哈希表p_busy，
#    分别存储当前闲着的面试官和忙着的面试官，元素都为一个pair，
#    pair[0] 保存已面试次数 pair[1] 保存面试结束时间；
# 3. 对所有的面试任务排序
# 4. 遍历所有的面试任务:
#    每轮从A中选一个面试官出来（选择已参加次数最少的面试官），
#    参加次数加一, 并更新结束时间后放进哈希表B中；
#    失败的情况：
#    1. p_free 没有人，说明人数不够。
#    2. p_free 中所有人的次数都用完了，说明人数不够。
# 5. 遍历完所有任务，成功则记录人数。
from heapq import heapify, heappop, heappush

def f1(m, n, tasks):
    # m 代表每位面试官最多面试的人
    # n 代表总面试次数
    # 对每一场面试按开始时间排序，开始时间相同的按照结束时间排序
    tasks = sorted(tasks, key=(lambda x: [x[0],x[1]]), reverse=False)
    print(tasks)
    l, r = n // m, n
    ans = n
    while l <= r:
        mid = (l + r) // 2 # 本次选择的面试官人数
        if can_make(mid, m, n, tasks):
            r = mid - 1
            ans = mid
        else:
            l = mid + 1
    return ans

def can_make(mid, m, n, tasks):
    # 记录每一位面试官已经面试的场次,和结束时间
    p_free = [[0,0] for _ in range(mid)] # 最小堆
    heapify(p_free)
    print(p_free)
    # 代表忙的面试官
    p_busy = []
    # 开始面试
    for i in range(n):
        start, end = tasks[i][0], tasks[i][1]
        if i == 0:
            item = heappop(p_free)
            if item[0]+1 <= m: # 面试次数+1
                p_busy.append([item[0]+1, end])
            else: return False
            continue
        for p in p_busy: # 有没有可以回归空闲的面试官
            if p[1] <= start:
                heappush(p_free, p)
                p_busy.remove(p)
        if len(p_free) == 0:
            return False # 即没有空闲的面试官
        else:
            item = heappop(p_free)
            if item[0]+1 <= m: # 还有面试次数
                p_busy.append([item[0]+1, end])
            else: return False
    return True

def test():
    # tasks 是开始时间和结束时间
    m, n = 3, 4
    info = [[1,2],[2,4],[2,3],[3,4]] # 2
    assert f1(m, n, info) == 2
    m, n = 2, 5
    info = [[1,2],[2,3],[3,4],[4,5],[5,6]] # 3
    assert f1(m, n, info) == 3
    m, n = 3, 3
    info = [[8,35],[5,10],[1,3]] # 2
    assert f1(m, n, info) == 2
    m, n = 2, 6
    info = [[0,5],[6,8],[0,2],[4,5],[1,7],[6,10]] # 4
    assert f1(m, n, info) == 4

if __name__ == '__main__':
    test()