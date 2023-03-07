# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.max1= float("-inf")
        
        def valid(node):
            
            if not node:

                return  True

            
            left = valid(node.left)
            
            if self.max1 >= node.val:
                
                return False
            
            self.max1 = node.val
            
            right = valid(node.right)
            
            return left and right
        
        return valid(root)
        
        

            
        