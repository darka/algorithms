class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0: 
            return []
        
        ret = [ [1] ]
        
        for i in xrange(2, numRows+1):
            lastRow = ret[-1]
            newRow = [1]
            
            for j in xrange(1, i-1):
                value = lastRow[j-1] + lastRow[j]
                newRow.append(value)
                
            newRow.append(1)
            
            ret.append(newRow)
            
        return ret
