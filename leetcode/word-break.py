class Solution:
  def wordBreak(self, s, dict):
    dict = set(dict)
    D = [False] * (len(s)+1)
    D[len(s)] = True
    for i in xrange(len(s), -1, -1):
      for j in xrange(i+1, len(s)+1):
        if s[i:j] in dict and D[j]:
          D[i] = True
    return D[0]
