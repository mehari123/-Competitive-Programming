# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        sum1 = 0

        def sumleft(root):

            if not root:

                return 

            nonlocal sum1
            if root.left and (root.left.left == None) and (root.left.right == None):

                sum1 += root.left.val

            sumleft(root.left)
            sumleft(root.right)
        sumleft(root)
        return sum1
        