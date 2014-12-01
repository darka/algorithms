class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs: 
            return ''
            
        lengthMin = min((len(i) for i in strs))
        index = 0
        
        for i in xrange(lengthMin):
            current = strs[0][i]
            finished = False
            for j in strs[1:]:
                if j[i] != current:
                    finished = True
                    break
                
            if finished:
                break
            else:
                index += 1
                
        return strs[0][0:index]
                
