# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
# 输入：head = [1,2,6,3,4,5,6], val = 6
# 输出：[1,2,3,4,5]
# 输入：head = [1,2,6,3,4,5,6], val = 6
# 输出：[1,2,3,4,5]
# 输入：head = [1,2,6,3,4,5,6], val = 6
# 输出：[1,2,3,4,5]
# 提示：
# 列表中的节点在范围 [0, 104] 内
# 1 <= Node.val <= 50
# 0 <= k <= 50
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 递归
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head
        head.next = self.removeElements(head.next, val)
        if head.val == val:
            next_node = head.next
        else:
            next_node = head
        return next_node

# 迭代
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        p = dummy
        while p is not None:
            if p.next and p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next