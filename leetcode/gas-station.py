class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canGoUntil(self, start, gas, cost):
        i = start
        current = 0
        
        while current >= 0:
            current += gas[i]
            current -= cost[i]
            i += 1
            i %= len(gas)
            if (i == start): 
                if current < 0: return -1 # we made a circle but couldn't get to the point
                break
        
        return i

    def canCompleteCircuit(self, gas, cost):
        i = 0
        while True:
            next = self.canGoUntil(i, gas, cost)
            if i == next: return i
            elif next < i: return -1
            else: i = next
            
        return -1

s = Solution()
print s.canCompleteCircuit([2,4],[3,4])
