class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        if needle == '': 
            return 0
            
        for i in xrange(len(haystack) - (len(needle)-1)):
            matches = 0
            for j in xrange(len(needle)):
                if haystack[i+j] == needle[j]:
                    matches += 1
                else:
                    break
            if matches == len(needle):
                return i
                
        return -1
        
