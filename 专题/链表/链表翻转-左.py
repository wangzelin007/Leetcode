def reverseLinkedList(head):
    pre = None
    next = None
    while head:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre