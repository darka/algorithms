# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if not p and not q:
            return True
            
        if p and q:
            if p.val != q.val:
                return False
            if self.isSameTree(p.left, q.left):
                return self.isSameTree(p.right, q.right)
                    
        return False
