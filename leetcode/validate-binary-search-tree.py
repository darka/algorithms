# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        if not root: return True
        return self.isValidBSTReal(root, float("-inf"), float("inf"))
        
    def isValidBSTReal(self, root, valMin, valMax):
        if not root: return True
        if root.left:
            if root.left.val >= root.val or root.left.val <= valMin:
                return False
            if not self.isValidBSTReal(root.left, valMin, root.val):
                return False
        if root.right:
            if root.right.val <= root.val or root.right.val >= valMax:
                return False
            if not self.isValidBSTReal(root.right, root.val, valMax):
                return False
        return True
        
