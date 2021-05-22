# https://leetcode-cn.com/problems/uncrossed-lines/solution/ni-de-yi-fu-wo-ba-liao-zui-chang-gong-gong-zi-xu-3/
# 在两条独立的水平线上按给定的顺序写下 nums1 和 nums2 中的整数。
# 现在，可以绘制一些连接两个数字 nums1[i]和 nums2[j]的直线，这些直线需要同时满足满足：
# nums1[i] == nums2[j]
# 且绘制的直线不与任何其他连线（非水平线）相交。
# 请注意，连线即使在端点也不能相交：每个数字只能属于一条连线。
# 以这种方法绘制线条，并返回可以绘制的最大连线数。
# 示例 1：
# 输入：nums1 = [1,4,2], nums2 = [1,2,4]
# 输出：2
# 解释：可以画出两条不交叉的线，如上图所示。
# 但无法画出第三条不相交的直线，因为从 nums1[1]=4 到 nums2[2]=4 的直线将与从 nums1[2]=2 到 nums2[1]=2 的直线相交。
# 示例 2：
# 输入：nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
# 输出：3
# 示例 3：
# 输入：nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
# 输出：2
# 提示：
# 1 <= nums1.length <= 500
# 1 <= nums2.length <= 500
# 1 <= nums1[i], nums2[i] <= 2000
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/uncrossed-lines
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

class Solution1:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        ans = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 从0开始计数
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return ans

# 718. 最长重复子数组
# 给两个整数数组A和B，返回两个数组中公共的、长度最长的子数组的长度。
# 示例：
# 输入：
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# 输出：3
# 解释：
# 长度最长的公共子数组是 [3, 2, 1] 。
# 提示：
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution2:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        ans = 0
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    ans = max(ans, dp[i][j])
        return ans

# 1143. 最长公共子序列
# 给定两个字符串text1 和text2，返回这两个字符串的最长 公共子序列 的长度。
# 如果不存在 公共子序列 ，返回 0 。
# 一个字符串的子序列是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
# 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
# 示例 1：
# 输入：text1 = "abcde", text2 = "ace"
# 输出：3
# 解释：最长公共子序列是 "ace" ，它的长度为 3 。
# 示例 2：
# 输入：text1 = "abc", text2 = "abc"
# 输出：3
# 解释：最长公共子序列是 "abc" ，它的长度为 3 。
# 示例 3：
# 输入：text1 = "abc", text2 = "def"
# 输出：0
# 解释：两个字符串没有公共子序列，返回 0 。
# 提示：
# 1 <= text1.length, text2.length <= 1000
# text1 和text2 仅由小写英文字符组成。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-common-subsequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        ans = 0
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return ans