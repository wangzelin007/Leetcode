# _*_ coding: utf-8 _*_
# 请实现 copyRandomList 函数，复制一个复杂链表。
# 在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。
#
# 示例 1：
# 输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
#
# 示例 2：
# 输入：head = [[1,1],[2,1]]
# 输出：[[1,1],[2,1]]
#
# 示例 3：
# 输入：head = [[3,null],[3,0],[3,null]]
# 输出：[[3,null],[3,0],[3,null]]
#
# 示例 4：
# 输入：head = []
# 输出：[]
# 解释：给定的链表为空（空指针），因此返回 null。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 哈希映射法
# {7:7',13:13',11:11',10:10',1:1'}
# dic[key].next = dic.get(key.next)
# dic[key].random = dic.get(key.random)
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head: return
        dic = {}
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        return dic[head]

# 辅助线法
# 7>7'>13>13'>11>11'>10>10'>1>1'
# 1. 复制各节点，构建拼接列表
# 2. 构建新节点的random指向
# if cur.random:
#     cur.next.random = cur.random.next
# cur = cur.next.next
# 3. 拆分两个列表
class Solution(object):
    def copyRandomList(self, head):
        if not head: return
        cur = head
        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        pre = head
        res = cur = head.next
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        # last'.next = None
        pre.next = None # last.next = last' > last.next = None
        return res

# 图的基本单元是 顶点，顶点之间的关联关系称为 边，我们可以将此链表看成一个图。
# 算法：深度优先搜索 DFS
# 从头结点 head 开始拷贝；
# 由于一个结点可能被多个指针指到，因此如果该结点已被拷贝，则不需要重复拷贝；
# 如果还没拷贝该结点，则创建一个新的结点进行拷贝，并将拷贝过的结点保存在哈希表中；
# 使用递归拷贝所有的 next 结点，再递归拷贝所有的 random 结点。
# 复杂度分析
# 时间复杂度：O(N)。
# 空间复杂度：O(N)。
class Solution:
    def copyRandomList(self, head):
        def dfs(head):
            if not head: return
            if head in visited:
                return visited[head]
            node = Node(head.val)
            visited[head] = node
            node.next = dfs(head.next)
            node.random = dfs(head.random)
            return node
        visited = {}
        return dfs(head)

# 算法：广度优先搜索 BFS
# 创建哈希表保存已拷贝结点，格式 {原结点：拷贝结点}
# 创建队列，并将头结点入队；
# 当队列不为空时，弹出一个结点，如果该结点的 next 结点未被拷贝过，则拷贝 next 结点并加入队列；同理，如果该结点的 random 结点未被拷贝过，则拷贝 random 结点并加入队列；
#
# 作者：z1m
# 链接：https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/solution/lian-biao-de-shen-kao-bei-by-z1m/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from collections import deque
class Solution:
    def copyRandomList(self, head):
        # bfs
        if not head: return
        head2 = Node(head.val)
        visited = {}
        q = deque()
        q.append(head)
        visited[head] = head2
        while q:
            tmp = q.popleft()
            if tmp.next and tmp.next not in visited:
                visited[tmp.next] = Node(tmp.next.val)
                q.append(tmp.next)
            if tmp.random and tmp.random not in visited:
                visited[tmp.random] = Node(tmp.random.val)
                q.append(tmp.random)
            visited[tmp].next = visited.get(tmp.next)
            visited[tmp].random = visited.get(tmp.random)
        return head2
