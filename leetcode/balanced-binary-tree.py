# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        _, balanced = self.depth(root, 0)
        return balanced
        
    def depth(self, root, currentDepth):
        if not root: 
            return currentDepth, True
        else:
            depthLeft, balancedLeft = self.depth(root.left, currentDepth + 1)
            depthRight, balancedRight = self.depth(root.right, currentDepth + 1)
            
            maxDepth = max(depthLeft, depthRight)
            
            if not balancedLeft or not balancedRight or math.fabs(depthLeft - depthRight) > 1:
                return maxDepth, False
                
            return maxDepth, True
        
