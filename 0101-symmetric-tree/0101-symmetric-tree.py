# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        
        def Symmetric( left,right):
            
            
            if not left and not right:
                
                return True
            
            elif (not left and right) or (not right and left):
                
                return False
            
            elif left.val != right.val:
            
                
                return False
            
            left1 = Symmetric(left.left,right.right)
            right1 = Symmetric(left.right,right.left)
            
            return left1 and right1
        
        return Symmetric(root.left,root.right)
            