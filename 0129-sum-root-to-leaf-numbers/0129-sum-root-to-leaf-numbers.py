# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        
        root_l = []
        
        def dfs(root,path):
            
            if not root:
                
                root_l.append(int(path[::]))
                return 
                
            path += str(root.val)
            
            if root.left and root.right:
                
                dfs(root.left,path)                      
                dfs(root.right,path)
                
            elif root.left:
                
                dfs(root.left,path)
                
            elif root.right:
                
                dfs(root.right,path)
                
            else:
                
                dfs(root.right,path)
                   
            path = path[:len(path) -1]
                              
            
        
        dfs(root,"")
        return sum(root_l)
                              
                              