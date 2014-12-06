import copy

class Solution:
  def wordBreak(self, s, dict):
    dict = set(dict)
    D = [False] * (len(s)+1)
    D[len(s)] = True
    for i in xrange(len(s), -1, -1):
      for j in xrange(i+1, len(s)+1):
        if s[i:j] in dict and D[j]:
          D[i] = True # Set to True if s[i..j] is a word and there is a word at s[j]
    
    results = self.produceSentences(0, D, s, dict)
    return [' '.join(result) for result in results]

  def produceSentences(self, i, D, s, dict, current=[]):
    results = []

    if i == len(D)-1:
      results.append(current)
    else:
      for j in xrange(i+1, len(D)):
        if s[i:j] in dict and D[j] == True:
          new = copy.copy(current)
          new.append(s[i:j])
          results.extend(self.produceSentences(j, D, s, dict, new))

    return results

s = Solution()
print s.wordBreak("catsanddog", ['cats', 'cat', 'sand', 'and', 'dog'])

