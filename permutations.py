import copy

class Solution:
  def permuteUnique(self, num):
    ret = set()
    self.gen(num, 0, ret)
    return list(list(i) for i in ret)
  
  def swap(self, seq, i, j):
    tmp = seq[i]
    seq[i] = seq[j]
    seq[j] = tmp
    
  # n is start of seq
  def gen(self, seq, n, results):
    if (n == len(seq)-1):
      results.add(tuple(copy.copy(seq)))
      return
    for i in xrange(n, len(seq)):
      if i != n and seq[i] == seq[n]:
        continue
      self.swap(seq, i, n)
      self.gen(seq, n+1, results)
      self.swap(seq, i, n)
    
sol = Solution()
results = sol.permuteUnique([1, 2, 2])
for result in results:
  print ''.join(str(i) for i in result)
