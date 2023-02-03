# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        prev=None
        
        dummy=head
        count1=head
        new_node=ListNode()
        new_head=new_node
        slow=head
        fast=head
        
        number_node=0
        
        while count1:
            number_node+=1
            count1=count1.next
        
    
        not_rev=number_node%k
        reverse_index=number_node-not_rev
        count=0
        print(not_rev)
        print(reverse_index)
        print(number_node)
        
        while dummy:
            
            index=0
            
            
            # print(prev)
            prev=None
            while index<k and dummy and (count<=reverse_index):
                
                temp=dummy.next
                dummy.next=prev
                prev=dummy
                dummy=temp
                
                index+=1
                count+=1
                if new_node and new_node.next:
                    new_node=new_node.next
            
            new_node.next=prev
            new_node=new_node.next
            if (count==reverse_index):
                reverse=new_head
                
                while reverse and reverse.next:
                    reverse=reverse.next
                reverse.next=dummy
                print(reverse)
                break
        
       
        return new_head.next
        
        
                
            
        
            
           
        