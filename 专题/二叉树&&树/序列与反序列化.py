from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def pres(head, ans):
    if not head:
        ans.append(None)
    else:
        ans.append(head.val) # 根据此位置该表为中序后序
        pres(head.left)
        pres(head.right)

def preb(prelist):
    prelist = deque(prelist)
    val = prelist.popleft()
    if not val:
        return None
    head = Node(val) # 根据此位置该表为中序后序
    head.left = preb(prelist)
    head.right = preb(prelist)
    return head

def levers(head, ans):
    if head is None:
        ans.append(None)
    else:
        q = [head]
        ans.append(head.val)
        while q:
            head = q.pop(0)
            if head.left:
                ans.append(head.left.val)
                q.append(head.left)
            else:
                ans.append(None)
            if head.right:
                ans.append(head.right.val)
                q.append(head.right)
            else:
                ans.append(None)
    return ans

def leverb(leverList):
    if leverList is None: return None
    head = Node(leverList.pop(0))
    q = []
    if head: q.append(head)
    while q:
        node = q.pop(0)
        left = leverList.pop(0)
        right = leverList.pop(0)
        node.left = Node(left) if left else None
        node.right = Node(right) if right else None
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
    return head

def test():
    head = Node(1)
    head.left = Node(2); head.right = Node(3)
    head.left.right = Node(4); head.right.left = Node(5)
    assert levers(head=head, ans=[]) == [1, 2, 3, None, 4, 5, None, None, None, None, None]
    assert levers(head=(leverb(leverList=[1, 2, 3, None, 4, 5, None, None, None, None, None])), ans=[]) == [1, 2, 3, None, 4, 5, None, None, None, None, None]


if __name__ == '__main__':
    test()