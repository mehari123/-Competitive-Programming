# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        level = defaultdict(lambda:[])
        
        
        def Level(root,row):
            
            if not root:
                
                return 
            
            
            level[row].append(root.val)
            
            Level(root.left,row + 1)
            
            Level(root.right,row +1)
            
            
            
        Level(root,0)
        
        level_o = []
        order = sorted(level)
        for o in order:
            
            level_o.append(level[o])
            
        return level_o
            
            