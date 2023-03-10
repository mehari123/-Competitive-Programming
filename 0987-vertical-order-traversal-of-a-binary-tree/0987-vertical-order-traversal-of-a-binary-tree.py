# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        Vert= defaultdict(lambda:[])
        Vertr= defaultdict(lambda:[])
        row=0
        
        def Vertical(root,row,col):
            
            if not root:
                
                return 
            
            Vert[col].append([root.val,row])
            Vertical(root.left,row+1,col-1)
            Vertical(root.right,row+1,col+1)
        
        Vertical(root,0,0)
        order= sorted(Vert)
        ans = []
        ans2 = []
        
        for index in order:

            ans.append(sorted(Vert[index]))
        
        for list1 in ans:
            
            list1 = sorted (list1,key = lambda x:x[1])
            list2 = [va[0] for va in list1 ]
            ans2.append(list2)
         
        return ans2
                             
            
            
            
            
        
        