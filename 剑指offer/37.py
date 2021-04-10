# _*_ coding: utf-8 _*_
# 请实现两个函数，分别用来序列化和反序列化二叉树。
# 示例:
# 你可以将以下二叉树：
#       1
#      / \
#     2   3
#        / \
#       4   5
#
# 序列化为 "[1,2,3,null,null,4,5]"
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Codec:
    # 序列化 Serialize ：
    # 借助队列，对二叉树做层序遍历，并将越过叶节点的 null 也打印出来。
    #
    # 算法流程：
    # 特例处理： 若 root 为空，则直接返回空列表 "[]" ；
    # 初始化： 队列 queue （包含根节点 root ）；序列化列表 res ；
    # 层序遍历： 当 queue 为空时跳出；
    # 节点出队，记为 node ；
    # 若 node 不为空：① 打印字符串 node.val ，② 将左、右子节点加入 queue ；
    # 否则（若 node 为空）：打印字符串 "null" ；
    # 返回值： 拼接列表，用 ',' 隔开，首尾添加中括号；
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        #       1
        #      / \
        #     2   3
        #        / \
        #       4   5
        if not root: return "[]"
        q = deque()
        q.append(root)
        res = []
        while q:
            tmp = q.popleft()
            if tmp:
                res.append(str(tmp.val))
                q.append(tmp.left)
                q.append(tmp.right)
            else:
                res.append('null')
        return '[' + ','.join(res) + ']'

    # 反序列化 Deserialize ：
    # 基于本文开始推出的 node , node.left , node.right 在序列化列表中的位置关系，可实现反序列化。
    # 利用队列按层构建二叉树，借助一个指针 i 指向节点 node 的左、右子节点，每构建一个 node 的左、右子节点，指针 i 就向右移动 1 位。
    #
    # 算法流程：
    # 特例处理： 若 data 为空，直接返回 null ；
    # 初始化： 序列化列表 vals （先去掉首尾中括号，再用逗号隔开），指针 i = 1 ，根节点 root （值为 vals[0] ），队列 queue（包含 root ）；
    # 按层构建： 当 queue 为空时跳出；
    # 节点出队，记为 node ；
    # 构建 node 的左子节点：node.left 的值为 vals[i] ，并将 node.left 入队；
    # 执行 i += 1 ；
    # 构建 node 的右子节点：node.left 的值为 vals[i] ，并将 node.left 入队；
    # 执行 i += 1 ；
    # 返回值： 返回根节点 root 即可；
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # ["1","2","3","null","null","4","5","null","null","null","null"]
        if data == '[]': return
        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if vals[i] != 'null':
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1
            if vals[i] != 'null':
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))