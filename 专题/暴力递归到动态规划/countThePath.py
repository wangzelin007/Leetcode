# 只能向下或者向右走，求总的走法
# dp[i][j] = dp[i-1][j] + dp[i][j-1]
# dp[i][j] = 0 if board[i][j] = '#'
# 然后需要逆向思维
# dp[i][j] 代表从 i，j 处出发到达 [m-1][n-1] 的方法数
# dp[i][j] = dp[i+1][j] + dp[i][j+1]

# 逆推
class Solution:
    def countThePaths(self, board):
        m, n = len(board), len(board[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][n-1] = 1
        for j in range(n):
            dp[m-1][j] = 1
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                if board[i][j] == '#':
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]

def test():
    board = [
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '#', '.', '.', '.', '#', '.'],
        ['.', '.', '.', '.', '#', '.', '.', '.'],
        ['#', '.', '#', '.', '.', '#', '.', '.'],
        ['.', '.', '#', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '#', '#', '.', '#', '.'],
        ['.', '#', '.', '.', '.', '#', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],]
    s = Solution()
    assert s.countThePaths(board) == 27

if __name__ == '__main__':
    test()