class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def getNextNode(node):
    if not node: return node
    if node.right:
        return getLeftMost(node.right)
    else:
        parent = node.parent
        while parent and parent.right == node:
            node = parent
            parent = node.parent
        return parent

def getLeftMost(node):
    if not node: return node
    while node.left:
        node = node.left
    return node

      # 0
    # 1   2
   # 3 4 5 6
def test():
    arr = [0, 1, 2, 3, 4, 5, 6]
    nodes = []
    for i in arr: nodes.append(Node(i))
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
    # 3 1 4 0 5 2 6
    assert getNextNode(nodes[3]) == nodes[1]
    assert getNextNode(nodes[1]) == nodes[4]
    assert getNextNode(nodes[4]) == nodes[0]
    assert getNextNode(nodes[0]) == nodes[5]
    assert getNextNode(nodes[5]) == nodes[2]
    assert getNextNode(nodes[2]) == nodes[6]
    assert getNextNode(nodes[6]) == None

if __name__ == '__main__':
    test()