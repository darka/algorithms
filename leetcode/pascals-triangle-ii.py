class Solution:
    # @return a list of integers
    
    def getRow(self, rowIndex):
        ret = [0] * (rowIndex + 1)
        ret[0] = 1
        
        for i in xrange(2, rowIndex + 2):
            for j in xrange(i-1, 0, -1):
                ret[j] += ret[j-1]
                
        return ret
        
