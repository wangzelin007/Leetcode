# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 前序遍历
# preorder

# 中序遍历
# inorder

# postorder
# 辅助栈
# 左右中 -> 中右左

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