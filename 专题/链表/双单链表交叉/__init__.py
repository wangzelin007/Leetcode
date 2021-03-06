# 哈希法

# 最终问题，判断两个链表是否相交
# 先判断 链表1 和 链表2 是否有环
# 判断方法快慢指针，确定相遇点
# 从 head 和相遇点同时出发，确定入环点

# 如果都无环，先走确定 长度L1 和 L2
# 长的先走 L1-L2 步，然后一起走，相交点即环入口点
# 优化没有必要记录两个长度，可以一个i++，一个i--。
# 优化如果有环，尾结点必须相等，且不为空
# 剑指offer 52 前提是无环！
# a+(b-c) = b+(a-c)

# 如果都有环
# 0. 独立的两个环 不相交
# 1. 入环点是同一个点 入环点即终点 然后等价于无环相交求交点。
# 2. 入环点是不同的点
# 0 2 两种情况，让其中任意一个入环点走一圈能碰到第二个入环点，说明相交
# 交点 入环点1 或者 入环点2 都可以

# 其他情况均不成立