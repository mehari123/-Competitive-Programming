# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        current=head
        slow=head
        fast=head
    
        while fast and fast.next:
            slow=slow
            slow=slow.next
            fast=fast.next.next        
      
        
        reverse_half=None
        
        while slow:
            temp_node=slow.next
            slow.next=reverse_half
            reverse_half=slow
            slow=temp_node
            
              
#         print("reverse_half")
#         print(reverse_half) 
#         print(head) 
        
#         print("slow")
#         print(slow) 
            
        while reverse_half:
            if reverse_half.val!=current.val:
                return False
            current=current.next
            reverse_half=reverse_half.next
        
        return True
            