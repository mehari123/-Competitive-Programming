# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dump = root
        def invert(Tree):

            if not Tree:

                return 

            temp = Tree.left
            Tree.left = Tree.right
            Tree.right = temp
            invert(Tree.left)
            invert(Tree.right)
        
        invert(root)
        return dump
        