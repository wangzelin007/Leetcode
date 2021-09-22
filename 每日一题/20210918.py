# You are playing the following Nim Game with your friend:
# Initially, there is a heap of stones on the table.
# You and your friend will alternate taking turns, and you go first.
# On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
# The one who removes the last stone is the winner.
# Given n, the number of stones in the heap, return true if you can win the game assuming both you and your friend play optimally, otherwise return false.
# Example 1:
# Input: n = 4
# Output: false
# Explanation: These are the possible outcomes:
# 1. You remove 1 stone. Your friend removes 3 stones, including the last stone. Your friend wins.
# 2. You remove 2 stones. Your friend removes 2 stones, including the last stone. Your friend wins.
# 3. You remove 3 stones. Your friend removes the last stone. Your friend wins.
# In all outcomes, your friend wins.
# Example 2:
# Input: n = 1
# Output: true
# Example 3:
# Input: n = 2
# Output: true
# Constraints:
# 1 <= n <= 231 - 1

# 1 2 3 先手必赢
# 4 后手必赢
# 5 1 + 4 先手赢
# 6 2 + 4 先手赢
# 7 3 + 4 先手赢
# 8 1 + 7 or 2 + 6 or 3 + 5 后手赢
# 9 1 + 8 or 2 + 7 or 3 + 6 先手赢
# 10 1 + 9 or 2 + 8 or 3 + 7 先手赢
# 11 1 + 10 or 2 + 9 or 3 + 8 先手赢
# 12 1 + 11 or 2 + 10 or 3 + 9 后手赢
# 13 1 + 12 or 2 + 11 or 3 + 10 先手赢
# 14 1 + 13 or 2 + 12 or 3 + 11 先手赢
# 15 1 + 14 or 2 + 13 or 3 + 12 先手赢
# 16 后手赢
# 三个先手赢 + 一个后手赢
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0

def test():
    s = Solution()
    assert s.canWinNim(1) is True
    assert s.canWinNim(14) is True
    assert s.canWinNim(15) is True
    assert s.canWinNim(12) is False

if __name__ == '__main__':
    test()
