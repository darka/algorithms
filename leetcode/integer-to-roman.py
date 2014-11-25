class Solution:
  def intToRoman(self, num):
    val = { 'M' : 1000, 'D' : 500, 'L' : 50, 'C' : 100, 'X': 10, 'I' : 1, 'V' : 5 }
    ordered_digits = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    final_result = ''

    for i in xrange(4):
      digits = ordered_digits[ i*2 : i*2 + 3] # Subset of digits we actually need
      result = ""
      digit = num / (10**i) % 10
      if digit <= 3:
        result += digits[0] * digit
      elif digit == 4:
        result += digits[0] + digits[1]
      elif digit <= 8:
        result += digits[1] + digits[0] * (digit % 5)
      else:
        result += digits[0] + digits[2]
      final_result = result + final_result
    return final_result

sol = Solution()
print sol.intToRoman(3999)
