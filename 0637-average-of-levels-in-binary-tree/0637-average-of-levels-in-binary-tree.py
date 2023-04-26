from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        de = deque()
        de.append(root)
        avarage = []
        
        def bfs(de):
            
        
            avarage.append(sum([d.val for d in de ])/len(de))
            deq = deque()
            
            while de:
                
                root = de.popleft()
                
                if root.left:
                    deq.append(root.left)
                if root.right:
                    
                    deq.append(root.right)
                
            if deq:
                
                bfs(deq)
            
        bfs(de)
        return avarage
            
            
            
        