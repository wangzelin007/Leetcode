# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 前序遍历
# preorder
# 递归
class Solution:
    def preorder(self, node):
        self.res = []
        self.healper(node, self.res)
        return self.res

    def healper(self, node, res):
        if not node:
            return
        res.append(node.val)
        self.healper(node.left, res)
        self.healper(node.right, res)

# 非递归
# preOrder每次都将遇到的节点压入栈，当左子树遍历完毕后才从栈中弹出最后一个访问的节点，访问其右子树。
# 在同一层中，不可能同时有两个节点压入栈，因此栈的大小空间为O(h)，h为二叉树高度。
# 时间方面，每个节点都被压入栈一次，弹出栈一次，访问一次，复杂度为O(n)。
def preOrder(self, root):
    if root == None:
        return
    myStack = []
    node = root
    while node or myStack:
        while node:
            # 从根节点开始，一直找它的左子树
            print node.val
            myStack.append(node)
            node = node.lchild
        # while结束表示当前节点node为空，即前一个节点没有左子树了
        node = myStack.pop()
        # 开始查看它的右子树
        node = node.rchild

# 中序遍历
# inorder
def inOrder(self, root):
    if root == None:
        return
    self.inOrder(root.lchild)
    print root.val
    self.inOrder(root.rchild)

# 根据上面的先序遍历，可以类似的构造出中序遍历。
# 仔细想一下，只有第一种方法改过来时最方便的。
# 需要的改动仅仅调换一下节点访问的次序，先序是先访问，再入栈；
# 而中序则是先入栈，弹栈后再访问。
def inOrder(self, root):
    if root == None:
        return
    myStack = []
    node = root
    while node or myStack:
        while node:
            # 从根节点开始，一直找它的左子树
            myStack.append(node)
            node = node.lchild
        # while结束表示当前节点node为空，即前一个节点没有左子树了
        node = myStack.pop()
        print node.val
        # 开始查看它的右子树
        node = node.rchild

# postorder
# 辅助栈
# 左右中 -> 中右左
def postOrder(self, root):
    if root == None:
        return
    self.postOrder(root.lchild)
    self.postOrder(root.rchild)
    print root.val

# 后序遍历对比中序遍历难度要增大很多。
# 因为中序遍历节点序列有一点的连续性，而后续遍历则感觉有一定的跳跃性。
# 先左，再右，最后才中间节点。
# 访问左子树后，需要跳转到右子树，右子树访问完毕了再回溯至根节点并访问之。
def later_stack(self, root):
    if root == None:
        return
    myStack1 = []
    myStack2 = []
    node = root
    myStack1.append(node)
    while myStack1:
        # 这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
        node = myStack1.pop()
        if node.lchild:
            myStack1.append(node.lchild)
        if node.rchild:
            myStack1.append(node.rchild)
        myStack2.append(node)
    while myStack2:
        # 将myStack2中的元素出栈，即为后序遍历次序
        print myStack2.pop().val

# postorder
# 双指针实现
# 一个指针负责子树的父节点，一个负责左右节点。

# 层序遍历
# 列表不为空循环
# 出队列打印，并入队左右子节点。

# 求二叉树最大的层宽
# 1. 节点入队时 map 标记每个 node 属于哪一层
# 2. 节点出队时 当前层总和 +1
# 3. 每层结束时结算currentMax并更新max
# 4. 最后一层需要单独结算

# 1. 当前层最右节点
# 2. 下一层最右节点
# 3. 当前层最大节点数 currentMax
# 4. 最大节点数max