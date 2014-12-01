# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum): 
        if not root: 
            return False
        return self.hasPath(root, sum, 0)
        
    def hasPath(self, root, sum, current):
        if not root.left and not root.right:
            return sum == current + root.val
            
        if root.left and self.hasPath(root.left, sum, current + root.val):
            return True
        elif root.right and self.hasPath(root.right, sum, current + root.val):
            return True
    
        return False
        
