# In an infinite binary tree where every node has two children, the nodes
# are labeeled in row order.
# In the odd numbered rows, the labelling is left to right,
# while in the even numbered rows, the labelling is right to left.
# Given the label of a node in this tree, return the labels in the path
# from the root of the tree to the node with that label.
# Input: label = 14
# Output: [1,3,4,14]
# Input: label = 26
# Output: [1,2,6,10,26]
from typing import List
from math import *

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        def reverse_label(label, h):
            return pow(2, h) + pow(2, h + 1) - label - 1
        ans = [label]
        h = int(log(label, 2))
        while label != 1:
            label = reverse_label(label, h) // 2
            ans.append(label)
            h -= 1
        ans.reverse()
        return ans




