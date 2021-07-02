class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Info:

    def __init__(self, b, h):
        self.isBalanced = b
        self.height = h

def isBalance(head):
    return process(head).isBalanced

def process(head):
    if not head: return Info(True, 0)
    leftInfo = process(head.left)
    rightInfo = process(head.right)
    height = max(leftInfo.height, rightInfo.height) + 1
    # isBalance = False if not leftInfo.isBalanced or not rightInfo.isBalanced or abs(leftInfo.height - rightInfo.height) > 1 else True
    isBalance = True if leftInfo.isBalanced and rightInfo.isBalanced and abs(leftInfo.height - rightInfo.height) <= 1 else False
    return Info(isBalance, height)

def test():
    #    0
    #  1   2
    # 3 4 5 6
    arr = [0, 1, 2, 3, 4, 5, 6]
    nodes = []
    for i in arr: nodes.append(TreeNode(i))
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[1].right = nodes[4]
    nodes[1].parent = nodes[0]
    nodes[2].left = nodes[5]
    nodes[2].right = nodes[6]
    nodes[2].parent = nodes[0]
    nodes[3].parent = nodes[1]
    nodes[4].parent = nodes[1]
    nodes[5].parent = nodes[2]
    nodes[6].parent = nodes[2]
    assert isBalance(nodes[0]) == True
    nodes[0].right = None
    assert isBalance(nodes[0]) == False

if __name__ == '__main__':
    test()
