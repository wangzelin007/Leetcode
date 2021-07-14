# 笔试
# 遍历两次
# 第一次的结构放入栈中，第二次和栈比较完全一致即可。

# 优化一半
# 快慢指针，快指针走完时，把慢指针走的剩下部分入栈。 == 右半部分逆序
# 从头开始遍历链表，当栈不为空时比较完全一致。

# 面试
# 1->2->3->2->1
# 我自己的思路是首先通过快慢指针，快指针走完时，慢指针来到中点
# 然后满指针向两边推进，看是否一致
# 难点：1. 区分奇偶 2. 向左走需要记录pre？

# O(1) 空间复杂度
# 所以需要进一步优化：
# 首先通过快慢指针，快指针走完时，慢指针来到中点
# 慢指针再继续走的时候，修改链表的指向。直到走完
# 从头和尾一起走，每一步都必须相等。
# 记得 recover 逆序的部分。。所以需要保存尾部(slow指针)的位置
class Solution:

    def isPalindrome(self, head):
        if head is None:
            return True

        first_half_end = self.end_of_first_half(head)
        secondHead = self.reverse_list(first_half_end.next)

        firstPosition = head
        secondPosition = secondHead

        result = True
        while firstPosition and secondPosition:
            if firstPosition.val != secondPosition.val:
                return False
            secondPosition = secondPosition.next
            firstPosition = firstPosition.next
        first_half_end.next = self.reverse_list(secondHead)
        return result

    def end_of_first_half(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_list(self, head):
        if not head or not head.next:
            return head
        pre = None
        next = None
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre