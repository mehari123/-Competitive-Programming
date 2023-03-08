# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        subtree=[]
        
        def findpath(root,path):
            
            if root.left == None and root.right == None:
                path += str(root.val)
                subtree.append(path)
                
                return
            
            path += str(root.val)+"->"
            if root.left:
                
                findpath(root.left,path)
                
            if root.right:
                
                findpath(root.right,path)
                
        findpath(root,"")
        return subtree
                