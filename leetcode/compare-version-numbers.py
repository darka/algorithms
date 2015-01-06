class Solution:
    def compareVersion(self, version1, version2):
        v1 = [int(i) for i in version1.split('.')]
        v2 = [int(i) for i in version2.split('.')]
        
        for i in xrange(max(len(v1), len(v2))):
            a = v1[i] if i < len(v1) else 0
            b = v2[i] if i < len(v2) else 0
                
            if a > b:
                return 1
            elif b > a:
                return -1
                
        return 0

