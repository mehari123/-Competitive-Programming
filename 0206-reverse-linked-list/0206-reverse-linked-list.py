# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        dummy_node=head
        
        while dummy_node:
            temp_node=dummy_node.next
            dummy_node.next=prev
            prev=dummy_node
            dummy_node=temp_node
            
        return prev
        
        
        