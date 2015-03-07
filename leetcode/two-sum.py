class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        diff = {}
        for i, n in enumerate(num):
            req = target - n
            if req in diff:
                return min(i, diff[req]) + 1, max(i, diff[req]) + 1
            diff[n] = i
