class Solution:
    def mergePattern(self, p):
        # Pattern optimiser: a*a*a* -> a*
        i = 1
        while i+2 < len(p):
          if p[i] == '*' and p[i+1] == p[i-1] and p[i+2] == '*':
            p = p[:i] + p[i+2:]
          else:
            i += 1
        return p
          
    def letterMatches(self, sc, pc):
        return pc == '.' or sc == pc
            
    def isMatch(self, s, p):
        p_new = self.mergePattern(p)
        table = [ [None]*(len(p)+1) for i in xrange(0, len(s)+1) ] # DP table
        ret = self.performMatch(s, p_new, 0, 0, table)
        return ret

    def performMatch(self, s, p, i, j, table):
        # Check for previously attemted match (DP)
        if table[i][j] != None: 
            return table[i][j]

        # Check if we finished matching
        if len(p) - j == 0:
            if len(s) - i == 0:
                return True

        elif len(p) - j > 1 and p[j+1] == '*':
            # Attempt to match 0 characters
            if self.performMatch(s, p, i, j+2, table):
                return True

            # Attempt to match >1 characters
            k = i
            while k < len(s) and self.letterMatches(s[k], p[j]):
                if self.performMatch(s, p, k+1, j+2, table):
                    return True
                k += 1

            # Full match (all possible characters)
            if self.performMatch(s, p, k, j+2, table):
                return True

        else:
            # Did we complete matching the string but the pattern is not finished?
            if i >= len(s): 
              table[i][j] = False
              return False

            # Simple case: match one letter
            if self.letterMatches(s[i], p[j]):
                return self.performMatch(s, p, i+1, j+1, table)

        # Store result in DP table
        table[i][j] = False
        return table[i][j]
        
                
sol = Solution()
print sol.isMatch("baccbbcbcacacbbc", "c*.*b*c*ba*b*b*.a*")

