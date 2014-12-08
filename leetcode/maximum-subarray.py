class Solution:
    def maxSubArray(self, A):
        largestSum = A[0]
        lastSum = A[0]
        for i in A[1:]:
            currentSum = max(lastSum + i, i)
            if currentSum > largestSum:
                largestSum = currentSum
            lastSum = currentSum
        return largestSum
