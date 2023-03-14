# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        
        level_order = defaultdict(lambda:[])
        
        
        def Level(root,row):
            
            if not root:
                
                return 
            
            level_order[row].append(root.val)
            Level(root.left,row + 1)
            Level( root.right,row +1)
         
        
        Level(root,0)
        order = sorted(level_order)
        ans = []
        
        for o in order:
            
            ans.append(level_order[o][-1])
            
        return ans
            
            
            
            