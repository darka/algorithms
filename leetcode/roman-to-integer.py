class Solution:
  # @return an integer
  def romanToInt(self, s):
    val = { 'M' : 1000, 'D' : 500, 'L' : 50, 'C' : 100, 'X': 10, 'I' : 1, 'V' : 5 }
    result = 0
    i = 0
    while i < len(s):
      if i + 1 < len(s) and val[s[i]] < val[s[i+1]]:
        result += (val[s[i+1]] - val[s[i]])
        i += 1
      else:
        result += val[s[i]]
      i += 1
    return result
 
sol = Solution()
print sol.romanToInt('MXXXVI')
        
