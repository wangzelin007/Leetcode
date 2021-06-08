# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。
# 如果两个链表没有交点，返回 null 。
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 公共部分为c
# 则 a + (b - c) = b + (a - c)
# 如果相交，位于交点处；如果不相交，位于 None 处
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A