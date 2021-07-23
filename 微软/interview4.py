class TreeNode(object):

    def __init__(self, left, right, value, index):
        self.left = left
        self.right = right
        self.value = value
        self.index = index

# 1. add node
# 2. delete node
# 3. get node
# 4. sift tree
class BinarySeachTree(object):

    def __init__(self, arr):
        self.head = self.add_node_by_arr(arr)

    def add_node_by_arr(self, arr):
        for val in arr:
            add_node(val)
        return head

    def add_node(self, value):
        sift_tree()

    def delete_node(self, value):
        # 如果删除head，选取比head小或者比head大的一个节点。
        node = self.get_max_node(self.head.left)
        self.head.value = node.value
        tmp = node.right
        node = tmp
        # 如果删除左子树的某一个node，选取比其大的一个node。
        # 如果删除右子树的某一个node，选取比其小的一个node。
        # 如果删除叶子节点，不需要调整。
        sift_tree()

    def get_node_by_value(self, value):
        return node

    def get_node_by_index(self, pos):
        return node

    def sift_tree(self):
        pass

    def get_max_node(self, head):
        return max_node

    def get_min_node(self, head):
        return min_node

def helper(arr, l, r):
    m = l + (r - l) // 2

# def test():
#     arr = [1, 2, 3, 4, 5, 6, 7]
#     head = generate_binary_tree(arr)
#     4
#   2   6
# 1  3 5  7

# 1,2,3,5,6,7
#           10
#      5           15
#    3   8      12     17
#   1 4 7  9  11  13 16   18
#               11.5


