# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        
        binary = TreeNode(preorder[0])
        
        def Bst (node,binary):

            if node < binary.val:

                if  binary.left == None:

                    binary.left = TreeNode(node)
                    return 

                Bst(node,binary.left)

            if node > binary.val:

                if binary.right == None:

                    binary.right =TreeNode(node)
                    return 

                Bst(node,binary.right)


        for i in preorder[1:]:
            
            Bst(i,binary)
            
        return binary