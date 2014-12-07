class Solution:
    def subsets(self, S):
        ret = []
        for i in xrange(2**len(S)):
            current = []
            n = 0
            while i > 0:
                if i & 1:
                    current.append(S[n])
                i >>= 1
                n += 1
            ret.append(sorted(current))
        return ret

