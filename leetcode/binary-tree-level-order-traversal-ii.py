# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if not root: 
            return []
            
        q = []
        ret = []
        q.append( (root, 0) )
        
        while len(q) > 0:
            top, d = q.pop(0)

            if top.left:
                q.append((top.left, d+1))
            if top.right:
                q.append((top.right, d+1))
                
            if d >= len(ret):
                ret.append([])
                
            ret[d].append(top.val)
            
        ret.reverse()    
        return ret
        
