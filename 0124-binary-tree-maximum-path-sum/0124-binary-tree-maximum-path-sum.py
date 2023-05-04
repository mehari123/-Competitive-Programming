# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.answer = -float('inf')
        def dfs(root):
            if not root:
                return -float('inf')
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            self.answer = max([self.answer, left, right, root.val, left+right+root.val])
            return max(left + root.val, right+root.val, root.val)
            
        return max(dfs(root), self.answer)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def to_graph(root):
            
#             if not root:
                
#                 return
            
#             if root.left and root.right:
                
#                 binary_graph[root.val].add(tuple([root.left.val,root.right.val]))
#                 to_graph(root.left)
#                 to_graph(root.right)
                
#             elif root.left and not root.right:
                
#                 to_graph(root.right)
#                 binary_graph[root.val].add(root.left.val)
                
#             elif root.right and not root.left:
#                 binary_graph[root.val].add(root.right.val)
#                 to_graph(root.left)
                
#             else:
                
#                 binary_graph[root.val].add(1001)
#                 to_graph(root.left)
        
#         to_graph(root)
#         print(binary_graph)
                
                
        