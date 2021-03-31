# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 类似的题目：39 40 46 47 70 78 90
# 结题思路：回溯 递归

# 70.子集
# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
#
# 示例 1：
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
# 示例 2：
# 输入：nums = [0]
# 输出：[[],[0]]
#
# 提示：
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# nums 中的所有元素 互不相同

# 迭代
class Solution1:
    def subsets(self, nums):
        res = [[]]
        # 多少位需要循环
        for i in nums:
            print res
            # res 代表没有i 时的各种组合
            # [[i]+num for num in res] 代表有i 时的各种组合
            # 即：
            # [[]] + [[1]] == [[],[1]]
            # [[],[1]] + [[2],[1,2]] == [[],[1],[2],[1,2]]
            # [[],[1],[2],[1,2]] + [[3],[1,3],[2,3],[1,2,3]] ==  [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
            # [0xx] + [1xx] = [xxx]
            res = res + [[i] + num for num in res]
            print res
        return res

# 递归
class Solution2:
    def subsets(self, nums):
        res = []
        n = len(nums)

        def dfs(i, tmp):
            print 'before',i,'tmp',tmp,'res',res
            res.append(tmp)
            print 'after res',res
            for j in range(i, n):
                dfs(j + 1, tmp + [nums[j]])
                #                        i:0 tmp:[] res:[].append([]) == [[]]
                # range(0,3)第一次   0+1 -> i:1 tmp:[]+[1] == [1] res:[[]].append([1]) == [[],[1]]
                # range(1,3)第一次   1+1 -> i:2 tmp:[1]+[2] == [1,2] res:[[],[1]].append([1,2]) == [[],[1],[1,2]]
                # range(2,3)第一次   2+1 -> i:3 tmp:[1,2]+[3] == [1,2,3] res: [[],[1],[1,2]].append([1,2,3]) ==  [[],[1],[1,2],[1,2,3]]
                # range(1,3)第二次   2+1 -> i:3 tmp:[1]+[3] == [1,3] res: [[],[1],[1,2],[1,2,3]].append([1,3]) == [[], [1], [1, 2], [1, 2, 3], [1, 3]]
                # range(0,3)第二次   1+1 -> i:2 tmp:[]+[2] == [2] res: [[], [1], [1, 2], [1, 2, 3], [1, 3]].append([2]) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2]]
                # range(2,3)第一次*2 2+1 -> i:3 tmp:[2]+[3] == [2,3] res: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2]].append([2,3]) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2,3]]
                # range(0,3)第三次   2+1 -> i:3 tmp:[]+[3] == [3] res: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2,3]].append([3]) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2,3], [3]]

        dfs(0, [])
        return res

# 90.子集II
# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
#
# 示例 1：
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
#
# 示例 2：
# 输入：nums = [0]
# 输出：[[],[0]]
#
# 提示：
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10

# 回溯法模板!!!
# res = []
# path = []
#
# def backtrack(未探索区域, res, path):
#     if path 满足条件:
#         res.add(path) # 深度拷贝
#         # return  # 如果不用继续搜索需要 return
#     for 选择 in 未探索区域当前可能的选择:
#         if 当前选择符合要求:
#             path.add(当前选择)
#             backtrack(新的未探索区域, res, path)
#             path.pop()

# 迭代
class Solution:
    def subsets(self, nums):
        res = [[]]
        nums.sort() #新增nums排序
        # 多少位需要循环
        for i in nums:
            print 'res',res
            # res 代表没有i 时的各种组合
            # [[i]+num for num in res] 代表有i 时的各种组合
            # 即：
            # [[]] + [[1]] == [[],[1]]
            # [[],[1]] + [[2],[1,2]] == [[],[1],[2],[1,2]]
            # [[],[1],[2],[1,2]] + [[3],[1,3],[2,3],[1,2,3]] ==  [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
            # [0xx] + [1xx] = [xxx]
            b = filter(lambda x: x+[i] not in res,res)
            print 'b',b
            res = res + [x+[i] for x in b]
            print 'ress',res
        return res

# 递归
class Solution2:
    def subsets(self, nums):
        res = []
        nums.sort() #新增nums排序
        n = len(nums)

        def dfs(i, tmp):
            print 'before',i,'tmp',tmp,'res',res
            res.append(tmp)
            print 'after res',res
            for j in range(i, n):
                if j > i and nums[j] == nums[j-1]: # 新增判断是否递归的条件！兄弟不能相等！
                    continue
                dfs(j + 1, tmp + [nums[j]])

        dfs(0, [])
        return res


if __name__ == '__main__':
    s = Solution()
    # s.subsets([1,2,2,3])
    s.subsets([1,2,2])
    # s = Solution2()
    # s.subsets([1,2,2,3])


