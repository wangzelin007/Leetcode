# Given an m x n board of characters and a list of strings words,
# return all words on the board.
# Each word must be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once in a word.
#
# Example 1:
# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
#
# Example 2:
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
from typing import List
import functools
from collections import Counter


#  超时
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.board = board
        self.tmp = []
        self.m, self.n = len(board), len(board[0])
        self.visited = [[False] * self.n for _ in range(self.m)]
        ans = []
        for i in range(self.m):
            for j in range(self.n):
                    self.visited[i][j] = True
                    self.findAllDirctions(i, j, board[i][j])
                    self.visited[i][j] = False
        for word in words:
            if word in self.tmp:
                ans.append(word)
        return ans

    # @functools.lru_cache(None)
    def findAllDirctions(self, i, j, cur):
        if len(cur) > 10:
            return
        self.tmp.append(cur)
        for x, y in self.directions:
            tx = i + x
            ty = j + y
            if 0 <= tx < self.m and 0 <= ty < self.n and not self.visited[tx][ty]:
                self.visited[tx][ty] = True
                self.findAllDirctions(i + x, j + y, cur + self.board[i + x][j + y])
                self.visited[tx][ty] = False

class Solution1:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(word, level, p, visited):
            if level == len(word):
                return True
            if p in visited or p[0] < 0 or p[0] == m or p[1] < 0 or p[1] == n:
                return False
            if board[p[0]][p[1]] == word[level]:
                visited.add(p)
                level += 1
                for dx, dy in (0, 1), (1, 0), (-1, 0), (0, -1):
                    if dfs(word, level, (p[0] + dx, p[1] + dy), visited):
                        return True
                visited.remove(p)
            return False


        m, n = len(board), len(board[0])
        cnts = Counter()
        for i in range(m):
            for j in range(n):
                cnts[board[i][j]] += 1
        ans = []
        for word in words:
            cur = Counter(word)
            canExists = True
            for c in cur:
                if cnts[c] < cur[c]:
                    canExists = False
                    break
            if not canExists:
                continue
            find = False
            for i in range(m):
                for j in range(n):
                    if dfs(word, 0, (i, j), set()):
                        ans.append(word)
                        find = True
                        break
                if find:
                    break
        return ans


# 不加lru超时
class Solution2:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n , m = len(board) , len(board[0])
        cnts = Counter()
        for i in range(n):
            for j in range(m):
                cnts[board[i][j]] += 1
        ans = []
        flag = [[0]*m for _ in range(n)]
        flag_find = [0]*len(words)
        # @functools.lru_cache() # 不能使用lru_cache，最后一个测试用例导致失败。
        def dfs(x,y,idx,idx_word):
            if idx == len(words[idx_word]) - 1:
                return True
            dir = [[1,0],[-1,0],[0,1],[0,-1]]
            for dirx , diry in dir:
                a = False
                tempx , tempy = x + dirx, y + diry
                if 0 <= tempx < n and 0 <= tempy < m and board[tempx][tempy] == words[idx_word][idx + 1] and flag[tempx][tempy] == 0:
                    flag[tempx][tempy] = 1
                    a = a or dfs(tempx, tempy, idx+1, idx_word)
                    flag[tempx][tempy] = 0
                    if a:
                        return a
            return a
        for idx ,word in enumerate(words) :
            cur = Counter(word)
            canExists = True
            for c in cur:
                if cnts[c] < cur[c]:
                    canExists = False
                    break
            if not canExists:
                continue
            find = False
            for i in range(n):
                for j in range(m):
                    if flag_find[idx] == 0 and board[i][j] == word[0]:
                        flag[i][j] = 1
                        if dfs(i, j, 0, idx):
                            flag_find[idx] = 1
                            ans.append(word)
                            find = True
                            flag[i][j] = 0
                            break
                        flag[i][j] = 0
                if find:
                    break
        return ans


class Solution3:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(word, idx, p, explored):
            if idx == len(word):
                return True
            if p in explored or p[0] < 0 or p[0] == m or p[1] < 0 or p[1] == n:
                return False
            if board[p[0]][p[1]] == word[idx]:
                explored.add(p)
                idx += 1
                for dx, dy in (0, 1), (1, 0), (-1, 0), (0, -1):
                    if dfs(word, idx, (p[0] + dx, p[1] + dy), explored):
                        return True
                explored.remove(p)
            return False

        m, n = len(board), len(board[0])
        cnts = Counter()
        for i in range(m):
            for j in range(n):
                cnts[board[i][j]] += 1
        ans = []
        for word in words:
            cur = Counter(word)
            canExists = True
            for c in cur:
                if cnts[c] < cur[c]:
                    canExists = False
                    break
            if not canExists:
                continue
            find = False
            for i in range(m):
                for j in range(n):
                    if dfs(word, 0, (i, j), set()):
                        ans.append(word)
                        find = True
                        break
                if find:
                    break
        return ans

def test():
    s = Solution2()
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    assert s.findWords(board, words) == ['oath', 'eat']
    board = [["a", "b"], ["c", "d"]]
    words = ["abcb"]
    assert s.findWords(board, words) == []
    board = [["o", "a", "b", "n"], ["o", "t", "a", "e"], ["a", "h", "k", "r"], ["a", "f", "l", "v"]]
    words = ["oa", "oaa"]
    assert s.findWords(board, words) == ["oa","oaa"]
    board = [["a", "a"]]
    words = ["aaa"]
    assert s.findWords(board, words) == []
    board = [["a", "b", "c", "e"],
             ["z", "z", "d", "z"],
             ["z", "z", "c", "z"],
             ["z", "a", "b", "z"]]
    words = ["abcdce"]
    assert s.findWords(board, words) == ["abcdce"]

if __name__ == '__main__':
    test()