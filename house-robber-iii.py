from collections import defaultdict
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        house = defaultdict(list)

        def traverse(root):
            if not root:
                return (0, 0)
            left = traverse(root.left)
            right = traverse(root.right)
            rob = root.val + left[1] + right[1]
            not_rob = max(left) + max(right)
            house[root].extend([rob, not_rob])
            return (rob, not_rob)

        traverse(root)
        return max(house[root])