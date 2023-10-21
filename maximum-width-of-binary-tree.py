# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        level_order = defaultdict(list)
        
        def LevelOrder(level,root,wid=1):

            if not root:
                return 
            
            level_order[level].append(wid)
            
            LevelOrder(level+1,root.left,wid*2)
            LevelOrder(level+1,root.right,wid*2+1)
            return
        
        LevelOrder(0,root)
        list_order = list(level_order.values())
        ans = 1
        
        for stack in list_order:
            ans = max(ans,stack[-1]- stack[0]+1)

        return ans