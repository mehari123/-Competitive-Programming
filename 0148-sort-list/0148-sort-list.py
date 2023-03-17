# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def divide (list1):
            
            if not list1.next or not head:
                
                return list1
            
            fast = list1
            slow = list1
            left_list = None
            
            while fast and fast.next:
                
                left_list = slow
                slow = slow.next
                fast = fast.next.next
                
            left_list.next = None 
            left = divide(list1)
            right = divide(slow)
            
            return merged1(left,right)
        
        def merged1(left,right):
            
            if not left and not right:
                
                return 
            
            elif not left:
                
                return right
            
            elif not right:
                
                return left
            
            elif left.val < right.val:
                
                left.next = merged1(left.next,right)
                return left
                
            else:
                
                right.next = merged1(left,right.next)
                return right
                
                
        
        return None if head == None else divide(head)
            
            
                
            
        