# _*_ coding: utf-8 _*_
# 0,1,···,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字（删除后从下一个数字开始计数）。
# 求出这个圆圈里剩下的最后一个数字。
# 例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。
#
# 示例 1：
# 输入: n = 5, m = 3
# 输出:3
#
# 示例 2：
# 输入: n = 10, m = 17
# 输出:2
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 约瑟夫环
# Fn = (Fn-1 + m) % len(Fn)

class Solution(object):
    def lastRemaining(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        x = 0
        for i in range(2, n+1):
            x = (x + m) % 1
        return x