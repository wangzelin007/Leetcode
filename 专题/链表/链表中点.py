# coding: utf-8
# 笔试的时候直接搞到list里面，不用用链表。
# 面试一定要使用链表写。

class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# 1. 返回基数长度中点或偶数长度上中点
def midOrUpMidNode(head):
    # None
    # 1
    # 1 2
    if not head or not head.next or not head.next.next:
        return head
    # 1 2 3
    # 1 2 3 4
    slow = head.next
    fast = head.next.next
    while (fast.next and fast.next.next):
        slow = slow.next
        fast = fast.next.next
    return slow
# 2. 返回基数长度中点或偶数长度下中点
def midOrDownMidNode(head):
    # None
    # 1
    if not head or not head.next:
        return head
    # 1 2
    # 1 2 3
    # 1 2 3 4
    slow = head.next
    fast = head.next
    while (fast.next and fast.next.next):
        slow = slow.next
        fast = fast.next.next
    return slow
# 3. 返回奇数长度中点前一个或偶数长度上中点前一个
def midOrUpMidPreNode(head):
    # None
    # 1
    # 1 2
    if not head or not head.next or not head.next.next:
        return None
    slow = head
    fast = head.next.next
    # 1 2 3
    # 1 2 3 4
    while (fast.next and fast.next.next):
        slow = slow.next
        fast = fast.next.next
    return slow
# 4. 返回奇数长度中点前一个或偶数长度下中点前一个
def midOrDownMidPreNode(head):
    # None
    # 1
    if not head or not head.next:
        return None
    # 1 2
    if not head.next.next:
        return head
    # 1 2 3 : 1
    # 1 2 3 4 : 2
    slow = head
    fast = head.next
    while (fast.next and fast.next.next):
        slow = slow.next
        fast = fast.next.next
    return slow

def create_test_data():
    head0 = LinkedNode(None)
    head1 = LinkedNode(1)
    head2 = LinkedNode(1)
    cur2 = head2
    for i in range(2, 3):
        cur2.next = LinkedNode(i)
        cur2 = cur2.next
    head3 = LinkedNode(1)
    cur3 = head3
    for i in range(2, 4):
        cur3.next = LinkedNode(i)
        cur3 = cur3.next
    head4 = LinkedNode(1)
    cur4 = head4
    for i in range(2, 5):
        cur4.next = LinkedNode(i)
        cur4 = cur4.next
    head5 = LinkedNode(1)
    cur5 = head5
    for i in range(2, 6):
        cur5.next = LinkedNode(i)
        cur5 = cur5.next
    return head0, head1, head2, head3, head4, head5

def test():
    res = create_test_data()
    assert midOrUpMidNode(res[0]).val == None
    assert midOrUpMidNode(res[1]).val == 1
    assert midOrUpMidNode(res[2]).val == 1
    assert midOrUpMidNode(res[3]).val == 2
    assert midOrUpMidNode(res[4]).val == 2
    assert midOrUpMidNode(res[5]).val == 3

    assert midOrDownMidNode(res[0]).val == None
    assert midOrDownMidNode(res[1]).val == 1
    assert midOrDownMidNode(res[2]).val == 2
    assert midOrDownMidNode(res[3]).val == 2
    assert midOrDownMidNode(res[4]).val == 3
    assert midOrDownMidNode(res[5]).val == 3

    assert midOrUpMidPreNode(res[0]) == None
    assert midOrUpMidPreNode(res[1]) == None
    assert midOrUpMidPreNode(res[2]) == None
    assert midOrUpMidPreNode(res[3]).val == 1
    assert midOrUpMidPreNode(res[4]).val == 1
    assert midOrUpMidPreNode(res[5]).val == 2

    assert midOrDownMidPreNode(res[0]) == None
    assert midOrDownMidPreNode(res[1]) == None
    assert midOrDownMidPreNode(res[2]).val == 1
    assert midOrDownMidPreNode(res[3]).val == 1
    assert midOrDownMidPreNode(res[4]).val == 2
    assert midOrDownMidPreNode(res[5]).val == 2

if __name__ == '__main__':
    test()