# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        left_node=head
        right_node=head
        current_l=head
        current_r=head
        sorted_head=None
        index=0
        index1=4
        right_head=None
        left_head=None
        
        if head==None:
            return head
        while current_l:
                # print(current_l.val,x)
                if current_l.val<x:
                
                    if index==0:
                        left_head=current_l
                        left_node=current_l
                    else:
                    
                        left_node.next=current_l
                        left_node=left_node.next
                    index=1
                    
                else:
                
                    if index1==4:
                        right_head=current_l
                        right_node=current_l
                    else:
                    
                        right_node.next=current_l
                        right_node=right_node.next
                            
                    index1=2
                current_l=current_l.next
        
        if right_head!=None:
            right_node.next=None
        

        if left_head==None:
             return right_head
        else:
            
            if right_head==None:
                return left_head
            else:
                left_node.next=right_head
                return left_head
        
        
    
            
        
        