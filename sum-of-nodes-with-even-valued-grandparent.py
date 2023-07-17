# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        total = 0

        def bfs(node):

            nonlocal total
            if not node:

                return 
            
            sum1 = 0
            if node.val % 2 == 0:

                if node.left:

                    if node.left.left:

                        sum1 += node.left.left.val

                    if node.left.right:

                        sum1 += node.left.right.val

                if node.right:

                    if node.right.left:

                        sum1 += node.right.left.val

                    if node.right.right:

                        sum1 += node.right.right.val

                total += sum1
            bfs(node.left)
            bfs(node.right)

        bfs(root)
        return total