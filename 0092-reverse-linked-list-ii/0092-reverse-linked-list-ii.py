# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        
        current=head
        index=1
        left_node=None
        if left==1:
            left_node=current
            
        while index<left:
            left_node=current
            current=current.next
            index+=1
        index=1
        right_node=None
        current=head
        while index<=right:
            right_node=current
            current=current.next
            index+=1
        # print(right_node)
        right_n=right_node.next
        left_n=left_node
        if left!=1:
            left_node=left_node.next
        else:
            pass
        
        reverse=right_node.next
        # print(right)
        while left_node!=right_n:
            
            temp_node=left_node.next
            left_node.next=reverse
            reverse=left_node
            left_node=temp_node
        
        
        if left==1:
            return reverse
        else:
            left_n.next=reverse
            return head
        
            
        
            
            