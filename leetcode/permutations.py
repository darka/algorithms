class Solution:
  def permute(self, num):
    ret = []
    self.gen(num, 0, ret)
    return ret
  
  def swap(self, seq, i, j):
    tmp = seq[i]
    seq[i] = seq[j]
    seq[j] = tmp
    
  def gen(self, seq, n, results):
    if n == len(seq) - 1:
      results.append(copy.copy(seq))
      return
  
    for i in xrange(n, len(seq)):
      self.swap(seq, i, n)
      self.gen(seq, n+1, results)
      self.swap(seq, i, n)
