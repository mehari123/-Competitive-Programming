# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
     
        current = head
        
        while current:
            
            sorted1 = head
            
            while sorted1 != current:
                
                if sorted1.val > current.val: 
                    
                    sorted1.val, current.val = current.val, sorted1.val
                    
                sorted1 = sorted1.next
                
            current = current.next
            
        return head
            
                    
                    
                    
                    
            