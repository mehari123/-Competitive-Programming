# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def Subtree(nodes):
            
            if not nodes:
                return False
            
            if self.sub_tree == pre_(nodes):
                return True
            
            left= Subtree(nodes.left)
            right = Subtree (nodes.right)
            
            return left or right
    
        def pre_(nodes):

            if not nodes:
                return []

            answer = [nodes.val]
            answer.append(pre_(nodes.left))
            answer.extend(pre_(nodes.right))

            return answer
        
        self.sub_tree = pre_(subRoot)
        return Subtree(root)

      
            
                           
                          