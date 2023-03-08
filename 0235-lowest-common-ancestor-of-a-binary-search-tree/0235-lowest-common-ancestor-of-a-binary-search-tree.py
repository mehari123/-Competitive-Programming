# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        def commen(root):
            
            root1= True if root.val in [p.val,q.val] else False
            left1 = findval(root.left)
            right1 = findval(root.right)
            # print(root1,left1,right1)
            if not root:

                return False
            
            if root1:
                
                return root
            
            if left1 and right1:

                return root
            
            elif left1 and not right1:
                
                return commen(root.left)
                
            elif not left1 and right1:
                
                return commen(root.right)
                
                
                
        
        def findval(node):

            if not node:

                return False
            
            # print(p,q,node.val)
            if node.val in [p.val,q.val]:

                return True

            return findval(node.left) or findval(node.right)
            
            
            
        
        return commen(root)
        