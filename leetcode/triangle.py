class Solution:
    def minimumTotal(self, triangle):
        for i in xrange(len(triangle)):
            for j in xrange(len(triangle[i])):
                possible = []
                if i > 0 and j != len(triangle[i]) - 1:
                    possible.append(triangle[i-1][j])
                if i > 0 and j > 0:
                    possible.append(triangle[i-1][j-1])
                if len(possible) > 0:
                    triangle[i][j] += min(possible)
        return min(triangle[-1])

