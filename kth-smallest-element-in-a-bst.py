# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        array = self.inorderTraversal(root.left)
        array.append(root.val)
        array += self.inorderTraversal(root.right)

        return array

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        array = self.inorderTraversal(root)
        return array[k - 1]