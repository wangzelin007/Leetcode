def removeValue(head, target):
    while head:
        if head.value != target:
            break
        head = head.next # 确定头部
    # 来到 head 不需要删的位置
    pre = head
    cur = head
    while cur:
        if cur.value == target:
            pre.next = cur.next
        else:
            pre = cur
        cur = cur.next