class Solution:
    def matches(self, c1, c2):
        return c1.upper() == c2.upper()
        
    def canBeIgnored(self, c):
        return not c.isalnum()

    def isPalindrome(self, s):
        i = 0
        j = len(s)-1
        
        while i < j and i < len(s) and j >= 0:
            
            while i < len(s) and self.canBeIgnored(s[i]): i+=1
            while j >= 0 and self.canBeIgnored(s[j]): j-=1
            
            if i >= len(s) or j < 0: 
                break
          
            if self.matches(s[i],s[j]):
                i += 1
                j -= 1
            else: 
                return False
            
        return i >= j
        
