# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        s_count =0
        sum1 = 0
        count1 = 0
        
        def avarage(root):
            
            nonlocal sum1, count1
            
            if not root:
                
                return 
            
            sum1 += root.val
            count1 += 1
            avarage(root.left)
            avarage(root.right)
            
            return sum1 // count1
        
        def Asubtree (root):
            
            nonlocal s_count,sum1, count1
            if not root:
                
                return 
            
            sum1 = 0
            count1 = 0
            if root.val == avarage(root):
                
                s_count += 1
            
            Asubtree(root.left)
            Asubtree(root.right)
            
            return s_count
        
        return Asubtree(root)
        
        
        