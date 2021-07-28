# ```
#      0
#     / \
#     1 2
#    / \
#    3 4
#     /
#    5
# ```
# The tree will be represented in a list, like `[-1, 0, 0, 1, 1, 4]`
# - The index of an element is the ID of the node
# - The value of an element is the parent node ID (-1 means this node doesn't have a parent which is the root node)
# Find the depth of the tree.
def findMaxDepth(arr):
    res = 0
    for idx, value in enumerate(arr):
        tmp = 0
        while value != -1:
            value = arr[value]
            tmp += 1
        res = max(res, tmp)
    return res

def test():
    arr = [-1, 0, 0, 1, 1, 4]
    print(findMaxDepth(arr))

if __name__ == '__main__':
    test()