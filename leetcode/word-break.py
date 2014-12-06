class Solution:
  def wordBreak(self, s, dict):
    dict = set(dict)
    D = [False] * len(s)
    for i in xrange(0, len(s)):
      for j in xrange(i+1, len(s)+1):
        if s[i:j] in dict and (i == 0 or D[i-1]):
          D[j-1] = True
    return D[-1]
