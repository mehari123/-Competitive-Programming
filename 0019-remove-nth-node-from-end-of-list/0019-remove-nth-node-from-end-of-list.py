# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        slow=head
        slow1=head
        fast=head
        count=0
        if head==None:
            return None
        
        delted_node=head
        
        while fast:
            fast=fast.next
    
            if count>n:
                slow=slow.next
                delted_node=slow.next.next
            if count==n:
                slow1=slow1.next
            count+=1
        print(slow)
        print(delted_node)
      
        if slow1==head and slow==head:
            return head.next
        elif slow1==head.next and slow==head:
            delted_node=head.next.next
            slow.next=delted_node
            return head
        else:
            slow.next=delted_node
            return head
            
            
        