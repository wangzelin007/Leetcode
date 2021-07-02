# 1. 与 head 无关
#    选取左树上最大距离 和 右树上最大距离的 最大值
# 2. 与 head 有关
#    左树高度 + 右树高度 + 1
class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Info:

    def __init__(self, m, h):
        self.maxDistance = m
        self.height = h

def maxDistance(head):
    return process(head).maxDistance

def process(head):
    if not head: return Info(0, 0)
    leftInfo = process(head.left)
    rightInfo = process(head.right)
    height = max(leftInfo.height, rightInfo.height) + 1
    maxDistance = max(leftInfo.height + rightInfo.height + 1, leftInfo.maxDistance, rightInfo.maxDistance)
    return Info(maxDistance, height)

