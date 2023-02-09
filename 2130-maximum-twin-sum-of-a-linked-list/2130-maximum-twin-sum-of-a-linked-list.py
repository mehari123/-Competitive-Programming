# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
    
        dummy=head
        new_node=ListNode(head.val)
        new_head=new_node
        reverse=None
        count1=0
        
        while dummy:
            
            new_temp=ListNode(dummy.val)
            new_node.next=new_temp
            new_node=new_node.next
            temp=dummy.next
            dummy.next=reverse
            reverse=dummy
            dummy=temp
            count1+=1
        
        orginal=new_head.next
        reversedd=reverse
        max1=float("-inf")
        index=0
        twin_sum=0
        
        while index<(count1//2):
            twin_sum=orginal.val+reversedd.val
            max1=max(max1,twin_sum)
            
            orginal=orginal.next
            reversedd=reversedd.next
            index+=1
            
        return max1