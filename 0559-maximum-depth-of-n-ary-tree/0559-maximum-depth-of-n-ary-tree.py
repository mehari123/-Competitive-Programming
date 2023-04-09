"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        

        def max_(root):
            
          
            if not root:
                
                return 0
            max1 = 0
            
            for child in root.children:
                
                max1 = max(max_(child),max1)
                
            return max1 + 1
        
        return max_(root)
            
            
            
        