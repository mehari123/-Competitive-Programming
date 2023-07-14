# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        count = 0
        
        def traverse(node):
            
            if not node:
                return 
            
            dfs(node,0)
            traverse(node.left)
            traverse(node.right)
            
        def dfs(curr_node,prev_sum):
            
            nonlocal count,targetSum
            
            if not curr_node:
                
                return
                
            prev_sum += curr_node.val
            
            if prev_sum == targetSum:
                
                count += 1
            
            dfs(curr_node.left,prev_sum)
            dfs(curr_node.right,prev_sum)
            
            prev_sum -= curr_node.val
            
        traverse(root)
        return count