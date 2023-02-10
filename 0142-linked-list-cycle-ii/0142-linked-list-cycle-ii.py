# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head==None:
            return 
        dummy=head
        fast=head.next
        slow=head
        contact_point=None
        
        #to be sure if there is cycle if there we will get the contact point
        while fast and fast.next:
            
            if fast==slow:
                contact_point=fast.next
                break
            
            fast=fast.next.next
            slow=slow.next
         
        # if fast and slow dosen't contact it mean no cyale return null
        if  contact_point==None:
            return 
        
        
        
        cycle_start=None
        index=0
        
        # finde the cycle strart point
        while head:
            
            if contact_point==head:
                return contact_point
            head=head.next
            contact_point=contact_point.next
            index+=1
        return 
            
        