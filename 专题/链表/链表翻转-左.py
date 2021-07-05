def reverseLinkedList(head):
    pre = None
    next = None
    while head:
        next = head.next
        head.next = pre
        pre = head
        head = next
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