# same with 1011
# 给你一个整数数组 jobs ，其中 jobs[i] 是完成第 i 项工作要花费的时间。
# 请你将这些工作分配给 k 位工人。
# 所有工作都应该分配给工人，且每项工作只能分配给一位工人。
# 工人的 工作时间 是完成分配给他们的所有工作花费时间的总和。
# 请你设计一套最佳的工作分配方案，使工人的 最大工作时间 得以 最小化 。
# 返回分配方案中尽可能 最小 的 最大工作时间 。
# 示例 1：
# 输入：jobs = [3,2,3], k = 3
# 输出：3
# 解释：给每位工人分配一项工作，最大工作时间是 3 。
# 示例 2：
# 输入：jobs = [1,2,4,7,8], k = 2
# 输出：11
# 解释：按下述方式分配工作：
# 1 号工人：1、2、8（工作时间 = 1 + 2 + 8 = 11）
# 2 号工人：4、7（工作时间 = 4 + 7 = 11）
# 最大工作时间是 11 。
# 提示：
# 1 <= k <= jobs.length <= 12
# 1 <= jobs[i] <= 107
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-minimum-time-to-finish-all-jobs
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution1:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        if k == len(jobs):
            return max(jobs)
        def dfs(num, groups, target):
            if not num:
                return True
            v = num.pop()
            print('groups', groups, 'target', target)
            for i, group in enumerate(groups):
                print('i', i, 'num', num, 'v', v)
                if group + v <= target:
                    groups[i] +=v
                    if dfs(num,groups,target): return True
                    groups[i] -=v # todo 不太明白
                if not group:  # 剪枝按照顺序分配
                    print('group', group)
                    break
            num.append(v) # todo 失败为什么要还原呢？还是不理解
            return False

        jobs.sort()
        i, j = jobs[-1],sum(jobs)
        while i < j :
            mid = i + (j-i)//2
            # print(i,j,mid)
            if dfs(jobs[:],[0]*k,mid): # 浅拷贝，只拷贝的外面的一层
                j = mid
            else:
                i = mid+1
        print(i)
        return i

# todo
class Solution2:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        def check(limit):
            # 剪枝：排序后，大的先拿出来试，如果方案不行，失败得更快
            arr = sorted(jobs)
            groups = [0] * k
            # 分成 K 组即 k 个工人，看看在这个limit 下 能不能安排完工作
            if backtrace(arr, groups, limit):
                return True
            else:
                return False

        def backtrace(arr, groups, limit):
            # 尝试每种可能性
            #print(arr, groups, limit)
            if not arr: return True #分完，则方案可行
            v = arr.pop()
            for i in range(len(groups)):
                if groups[i] + v <= limit:
                    groups[i] += v
                    if backtrace(arr, groups, limit):
                        return True
                    groups[i] -= v
                    # 剪枝，如果这个工人没分到活，那别人肯定得多干活了，那最后的结果必然不是最小的最大值，就不用继续试了。
                    if groups[i] ==0:
                        break

            arr.append(v)
            return False

        #每个人承担的工作的上限，最小为，job 里面的最大值，最大为 jobs 之和
        l, r  = max(jobs), sum(jobs)
        while l < r:
            mid = (l + r)//2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l

# todo
class Solution3:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        #贪心求一个次优解
        from heapq import heapify,heappush,heappop
        heap = [0]*k
        heapify(heap)
        jobs = sorted(jobs)[::-1]
        for i in jobs:
            heappush(heap, heappop(heap)+i)
        m = max(heap)

        a = [0]*k  # k 个工人，每个工人的工作量，初始为 0
        def job(j):
            nonlocal m
            if j == len(jobs):
                m = min(m,max(a))   #记录已知最优解
                return
            for i in range(min(k,j+1)): #剪枝，第 j 个工作只能分配给前 j 个工人
                if a[i]+jobs[j]>m:  #如果工作 j 分配给工人 i 后，工人 i 工作量大于已知最优解 m ，跳过
                    continue
                a[i] += jobs[j]
                job(j+1)
                a[i] -= jobs[j]
        job(0)
        return m

if __name__ == '__main__':
    s = Solution1()
    jobs = [3,2,3]; k = 3
    s.minimumTimeRequired(jobs, k)
    jobs = [1,2,4,7,8]; k = 2
    s.minimumTimeRequired(jobs, k)