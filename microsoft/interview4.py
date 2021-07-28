class TreeNode(object):

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 缺点是不够平衡，层数过多。
class BinarySeachTree(object):

    def insert(self, root, val):
        if not root:
            root = TreeNode(val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        return root

    def query(self, root, val):
        if not root:
            return False
        if root.val == val:
            return True
        elif val < root.val:
            return self.query(root.left, val)
        elif val > root.val:
            return self.query(root.right, val)

    def findMin(self, root):
        if root.left:
            return self.findMin(root.left)
        else:
            return root

    def findMax(self, root):
        if root.right:
            return self.findMax(root.right)
        else:
            return root

    def delNode(self, root, val):
        if not root:
            return
        if val < root.val:
            root.left = self.delNode(root.left, val)
        elif val > root.val:
            root.right = self.delNode(root.right, val)
        # val == root.val 1. both 2. both empty 3. only left 4. only right
        else:
            if root.left and root.right:
                # 左右子树都存在，查找右子树最小值
                temp = self.findMin(root.right)
                root.val = temp.val
                # 替换后，把右子树中最小值节点删除
                root.right = self.delNode(root.right, temp.val)
            elif not root.left and not root.right:
                # 都为空说明是唯一节点
                root = None
            elif not root.right:
                # 只有左子树
                root = root.left
            elif not root.left:
                # 只有右子树
                root = root.right
        return root


    def printTree(self, root):
        # 中序遍历
        if not root:
            return
        self.printTree(root.left)
        print(root.val, end=' ')
        self.printTree(root.right)

def test():
    arr = [7, 4, 3, 2, 5, 6, 1]
    bst = BinarySeachTree()
    # root = bst.insert(None, 1)
    # root = bst.insert(root, 2)
    # root = bst.insert(root, 3)
    # root = bst.insert(root, 4)
    # root = bst.insert(root, 5)
    # root = bst.insert(root, 6)
    # root = bst.insert(root, 7)
    # insert
    root = None
    for i in arr:
        root = bst.insert(root, i)
    # query
    assert bst.query(root, 5) is True
    assert bst.query(root, 8) is False
    # finMin finMax
    assert bst.findMin(root).val == 1
    assert bst.findMax(root).val == 7
    # print
    bst.printTree(root)
    # delete
    root = bst.delNode(root, 5)
    bst.printTree(root)

if __name__ == '__main__':
    test()
#     4
#   2   6
# 1  3 5  7

# 1,2,3,5,6,7
#           10
#      5           15
#    3   8      12     17
#   1 4 7  9  11  13 16   18
#               11.5


