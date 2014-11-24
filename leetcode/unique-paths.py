class Solution:
  # @return an integer
  def uniquePaths(self, m, n):
    if m == 0 or n == 0: return 0
    board = [[0]*n for i in xrange(m)]
    board[m-1][n-1] = 1
    for i in reversed(xrange(0, n)):
      for j in reversed(xrange(0, m)):
        paths = board[j][i]
        if i+1 < n:
          paths += board[j][i+1]
        if j+1 < m:
          paths += board[j+1][i]
        board[j][i] = paths
    return board[0][0]

sol = Solution()
print sol.uniquePaths(0, 0)
