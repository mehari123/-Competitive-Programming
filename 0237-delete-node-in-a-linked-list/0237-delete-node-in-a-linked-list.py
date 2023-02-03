# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        count=0
        dummy=node
        
        while dummy:
            count+=1
            dummy=dummy.next
            if count>=3:
                break
                
        if count==2:
            
            node.val=node.next.val
            node.next=None
            
        else:
            
            while node:
                
                node.val=node.next.val
                node=node.next
                count+=1
                
                if node.next.next==None:
                    node.val=node.next.val
                    node.next=None
                    break
        
        