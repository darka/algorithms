class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        last_seen = {}
        
        length_max = 0
        length_current = 0
        start = 0
        
        for n, i in enumerate(s):
            seen = last_seen.get(i, -1)
            length_current += 1
            
            if seen >= start:
                start = seen + 1
                length_current = n - seen
            
            if length_current > length_max:
                length_max = length_current
                
            last_seen[i] = n
            
        return length_max
