# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dummy = head
        
        while dummy and dummy.val == val:
            
            dummy = dummy.next
            
        head = dummy
            
        while head and head.next:
            
            if head.next.val == val:
                temp = head
                while head.next and head.next.val == val:
                    
                    head = head.next
                    
                if head.next:
                    
                    temp.next = head.next
                    head = temp
                else:
                    
                    temp.next = None
                    head =  temp
                    
            head = head.next
                    
        return dummy
            
                
                
                
                
        