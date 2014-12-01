class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if not s: 
            return 0
            
        s = s.rstrip()
        i = len(s) - 1
        
        length = 0
        while i >= 0 and s[i] != ' ': 
            i -= 1
            length += 1
            
        return length
        
