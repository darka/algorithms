class Solution:
    def isLegal(self, s, i, j):
        if j < 0 or i < 0: 
            return False
        if i > len(s) or j > len(s): 
            return False
        if j - i > 1 and s[i] == '0':
            return False
        if int(s[i:j]) <= 255: 
            return True
        return False
        
    def restoreRest(self, s, start, parts_left, current):
        ret = []
        if parts_left == 0:
            if len(current) == 4 and start == len(s):
                ret.append(current)
        else:
            for i in xrange(1, 4):
                next = copy.copy(current)
                if self.isLegal(s, start, start+i):
                    next.append(s[start:start+i])
                    ret.extend(self.restoreRest(s, start+i, parts_left - 1, next))
        return ret

    def restoreIpAddresses(self, s):
        ips = self.restoreRest(s, 0, 4, [])
        return ['.'.join(n) for n in ips]

