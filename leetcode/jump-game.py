class Solution:
  def canJump(self, A):
    if not A: 
      return false

    furthest = A[0]

    for n, i in enumerate(A[1:]):
      n = n+1
      if n > furthest:
        return False
      furthest = max(furthest, n+i)
      if furthest >= len(A)-1:
        return True

    return True

sol = Solution()
print sol.canJump([2,3,1,1,4])
print sol.canJump([3,2,1,0,4])
print sol.canJump([0])

