def reverseLinkedList(head):
    pre = None
    next = None
    while head:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre

# 简洁写法
def reverseLinkedList(head):
    pre, cur = None, head
    while cur:
        # 交换写法不需要中间变量
        cur.next, pre, cur = pre, cur, cur.next
    return pre

# 双指针链表
def reverseLinkedList(head):
    pre = None
    next = None
    while head:
        next = head.next
        head.next = pre
        head.last = next
        pre = head
        head = next