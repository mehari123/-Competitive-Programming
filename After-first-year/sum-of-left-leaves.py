# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        left_sum = 0
        def sumleft(node,side):

            left_sum = 0
            if not node.left  and  not node.right and side == "L":

                return node.val

            elif not node.left  and  not node.right and side == "R":

                return 0

            elif node.left and node.right:

                left_sum += sumleft (node.left,"L") + sumleft (node.right,"R")

            elif node.left and not node.right:

                left_sum += sumleft(node.left,"L")

            elif node.right and not node.left:

                left_sum += sumleft(node.right,"R")

            return left_sum

        
        return sumleft(root,"R")
        