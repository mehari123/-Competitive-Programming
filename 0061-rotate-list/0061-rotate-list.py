# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy=head
        count_node=0
    
        while dummy:
            
            count_node+=1
            dummy=dummy.next
        
        
        
        if count_node==0:
            return 
        else:
            rotate=k%count_node
        print(rotate)
        if count_node==1 or rotate==0 or rotate==count_node:
            return head
        index=0
        rotate=count_node-rotate
        right=head
        left=head
        
        while index<rotate-1:
            
            left=left.next
            right=right.next
            index+=1
        
       
        right=right.next
        left.next=None
        rotated_head=right
     
        while right:
        
            if right.next==None:
            
                right.next=head
                break
                
            right=right.next
            
        return rotated_head
            
        
        
    
        
        
        
        
        
        