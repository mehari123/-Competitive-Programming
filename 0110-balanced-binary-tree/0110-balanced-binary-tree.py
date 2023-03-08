# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def Balannced (root):
            
            if not root:
                return True
            
            lefth = findH(root.left)
            righth = findH(root.right)
            
            if abs(lefth-righth)>1:
                
                return False
            
            left= Balannced (root.left)
            right=Balannced (root.right)
            
            return left and right

        def findH(root):
            
            if not root:
                
                return 0
            
            height = 1
            
            height += max(findH(root.left),findH(root.right))
            
            return height
        
        return Balannced (root)
            
            
        