class Solution:
    def maxPathSum(self, root):
        self.maxSum = None
        self.maxPathSumRec(root)
        return self.maxSum
        
    def maxPathSumRec(self, root):
        if not root:
            return 0
        leftSum = max(self.maxPathSumRec(root.left), 0)
        rightSum = max(self.maxPathSumRec(root.right), 0)
        
        candidate = leftSum + root.val + rightSum
        if self.maxSum == None:
            self.maxSum = candidate
        else:
            self.maxSum = max(self.maxSum, candidate)
        return root.val + max(leftSum, rightSum)
    