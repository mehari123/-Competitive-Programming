# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.root = root
        if root == None:
            
            return  TreeNode(val,None,None)
            
        def insertNode(node,val):  
            
            if node:
                
                if node.val > val:
                    
                    if node.left==None:
                    
                        new_node = TreeNode(val,None,None)

                        node.left = new_node

                        return 
                    
                    insertNode(node.left,val)
                    return
                    
                    
                else :
                    
                    if node.right == None:
                        

                        new_node = TreeNode(val,None,None)

                        node.right = new_node

                        return 
                    insertNode(node.right,val)
                    return

        insertNode(self.root,val)
        
        return self.root