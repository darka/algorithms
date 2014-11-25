class Interval:
    def __init__(self, ls):
        self.start = ls[0]
        self.end = ls[1]
    def __repr__(self):
        return "Interval([{}, {}])".format(self.start, self.end)

class Solution:
    def merge(self, intervals):
        if not intervals: 
            return []
            
        intervals.sort(cmp=lambda a, b : cmp([a.start, a.end], [b.start, b.end]))
        
        ret = []
        current = intervals[0]
        
        i = 1
        
        while i < len(intervals):
            next = intervals[i]
            if current.end >= next.start:
                if next.end > current.end:
                    current.end = next.end
            else:
                ret.append(current)
                current = next
            i += 1
            
        ret.append(current)
        
        return ret

sol = Solution()
print sol.merge([ Interval([1,3]), Interval([2,6]), Interval([8, 10]), Interval([15, 18]) ])
print sol.merge([ Interval([1,4]), Interval([1,4]) ])
