# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def traverse(node):

            if not node:
                return "#"
            
            # Get the subtree structures of the left and right subtrees
            left_structure = traverse(node.left)
            right_structure = traverse(node.right)
            
            # Combine the current node's value, left subtree structure, and right subtree structure
            subtree_structure = str(node.val)  + "#" + left_structure + "#" +  right_structure
            
            # Add the subtree structure to the hash map and update its frequency
            subtree_counts[subtree_structure] += 1
            
            # If the frequency becomes 2, add the current node to the result list
            if subtree_counts[subtree_structure] == 2:
                result.append(node)
            print(subtree_structure)
            return subtree_structure

        # Initialize variables
        result = []
        subtree_counts = defaultdict(int)
        
        # Start the traversal
        traverse(root)
        
        return result