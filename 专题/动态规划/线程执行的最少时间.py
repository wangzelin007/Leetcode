# 动态规划
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        # k 代表线程数量
        #---------------------检查当前threshold是否能完成----------------------------#
        def check(threshold : int) -> bool:
            worker = [0 for _ in range(k)]
            #--------------回溯----------------#
            def backtrace(idx: int) -> bool:
                if idx == jobLen:
                    return True
                for i in range(k):
                    if worker[i] + jobs[idx] <= threshold:
                        worker[i] += jobs[idx]
                        if backtrace(idx + 1) == True:
                            return True
                        worker[i] -= jobs[idx]
                    if worker[i] == 0:      #如果当前的没分配上。后面的也分配不上。因为job从大到小
                        break
                    if worker[i] + jobs[idx] == threshold:  #当前就是最优，没必要再往后了
                        break
                return False

            return backtrace(0)

        jobs.sort(reverse = True)
        jobLen = len(jobs)
        L = max(jobs)
        R = sum(jobs)
        while L < R:
            mid = (L + R) // 2
            if check(mid) == True:
                R = mid
            else:
                L = mid + 1
        return L