# 给定一颗二叉树的头节点head
# 返回这颗二叉树中最大二叉搜索子树的节点数
class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Info:

    def __init__(self, i, m, b, s):
        self.isBST = i
        self.maxSubBSTSize = m
        self.big = b
        self.small = s


def maxSubBSTSize(head):
    if not head: return 0
    return process(head).maxSubBSTSize

def process(head):
    if not head: return None
    leftInfo = process(head.left)
    rightInfo = process(head.right)
    big, small = head.value, head.value
    maxSubBSTSize = 0
    if leftInfo:
        big = leftInfo.big
        small = leftInfo.small
        maxSubBSTSize = max(maxSubBSTSize, leftInfo.maxSubBSTSize)
    if rightInfo:
        big = max(big, rightInfo.big)
        small = min(small, rightInfo.small)
        maxSubBSTSize = max(maxSubBSTSize, rightInfo.maxSubBSTSize)
    isBST = False
    if (True if leftInfo == None else leftInfo.isBST and leftInfo.big < head.value) and \
       (True if rightInfo == None else rightInfo.isBST and rightInfo.small > head.value):
        isBST = True
        maxSubBSTSize = (leftInfo.maxSubBSTSize if leftInfo else 0) \
                        + (rightInfo.maxSubBSTSize if rightInfo else 0) + 1
    return Info(isBST, maxSubBSTSize, big, small)

def test():
    #    3
    #  1   5
    # 0 2 4 6
    # arr = [0, 1, 2, 3, 4, 5, 6]
    arr = [3, 1, 5, 0, 2, 4, 6]
    nodes = []
    for i in arr: nodes.append(TreeNode(i))
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[1].right = nodes[4]
    nodes[2].left = nodes[5]
    nodes[2].right = nodes[6]
    print(maxSubBSTSize(nodes[0]))
    # assert maxSubBSTSize(nodes[0]) == 1
    assert maxSubBSTSize(nodes[0]) == 7

if __name__ == '__main__':
    test()


