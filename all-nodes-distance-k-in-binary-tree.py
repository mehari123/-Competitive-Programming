# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        result = []
        
        def find_target(root, k):
            if not root:
                return -1
            
            if root.val == target.val:
                find_nodes_down(root, k)
                return 0
            
            left_distance = find_target(root.left, k)
            if left_distance != -1:
                if left_distance + 1 == k:
                    result.append(root.val)
                else:
                    find_nodes_down(root.right, k - left_distance - 2)
                return left_distance + 1
            
            right_distance = find_target(root.right, k)
            if right_distance != -1:
                if right_distance + 1 == k:
                    result.append(root.val)
                else:
                    find_nodes_down(root.left, k - right_distance - 2)
                return right_distance + 1
            
            return -1
        
        def find_nodes_down(root, k):
            if not root or k < 0:
                return
            
            if k == 0:
                result.append(root.val)
                return
            
            find_nodes_down(root.left, k - 1)
            find_nodes_down(root.right, k - 1)
        
        find_target(root, k)
        return result