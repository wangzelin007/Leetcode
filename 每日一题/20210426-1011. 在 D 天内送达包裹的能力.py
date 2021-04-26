# 传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。
# 传送带上的第 i个包裹的重量为weights[i]。
# 每一天，我们都会按给出重量的顺序往传送带上装载包裹。
# 我们装载的重量不会超过船的最大运载重量。
# 返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。
# 示例 1：
# 输入：weights = [1,2,3,4,5,6,7,8,9,10], D = 5
# 输出：15
# 解释：
# 船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
# 第 1 天：1, 2, 3, 4, 5
# 第 2 天：6, 7
# 第 3 天：8
# 第 4 天：9
# 第 5 天：10
# 请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 是不允许的。
# 示例 2：
# 输入：weights = [3,2,2,4,1,4], D = 3
# 输出：6
# 解释：
# 船舶最低载重 6 就能够在 3 天内送达所有包裹，如下所示：
# 第 1 天：3, 2
# 第 2 天：2, 4
# 第 3 天：1, 4
# 示例 3：
# 输入：weights = [1,2,3,1,1], D = 4
# 输出：3
# 解释：
# 第 1 天：1
# 第 2 天：2
# 第 3 天：3
# 第 4 天：1, 1
# 提示：
# 1 <= D <= weights.length <= 50000
# 1 <= weights[i] <= 500
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
# 读题能力还是需要提高的
# 求解：一个满足D天运送完的运载能力
# 最小运载力 max(weights) 最大运载力 sum(weights)
# 二分法 如果 need < D 减小运载力；如果 need > D 增加运载力
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            need, cur = 1, 0
            for weight in weights:
                if cur + weight > mid:
                    need += 1
                    cur = 0
                cur += weight
            # 为什么不能提前返回
            # need <= D 满足的肯定在 <= mid 里面，所以 right = mid
            # need > D 满足的肯定在 mid 右边，所以 left = mid + 1
            # 知道left = right 才能确定满足条件的最小运载力
            if need <= D:
                # 降低运载能力
                right = mid
            else:
                # 提高运载能力
                left = mid + 1
        return left

# todo 精确边界
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        max_w, sum_w = max(weights), sum(weights)
        l, r = max(max_w, sum_w // D), sum_w
        while l < r:
            mid = (l + r) >> 1
            if self.check(weights, mid, D):
                r = mid
            else:
                l = mid + 1
        return r

    def check(self, ws, t, d):
        n = len(ws)
        i = cnt = 1
        total = ws[0]
        while i < n:
            while i < n and total + ws[i] <= t:
                total += ws[i]
                i += 1
            total = 0
            cnt += 1
        return cnt - 1 <= d

if __name__ == '__main__':
    s = Solution()
    # weights = [1,2,3,4,5,6,7,8,9,10]; D = 5 # 15
    # print(s.shipWithinDays(weights, D))
    # weights = [3,2,2,4,1,4]; D = 3 # 6
    # print(s.shipWithinDays(weights, D))
    # weights = [1,2,3,1,1]; D = 4 # 3
    # print(s.shipWithinDays(weights, D))
    weights = [10,50,100,100,50,100,100,100]; D = 5
    print(s.shipWithinDays(weights, D)) # 160


