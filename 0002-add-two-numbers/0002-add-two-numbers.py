# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        number1=""
        number2=""
    
        # get number 1
        while l1:
            
            number1+=str(l1.val)
            l1=l1.next
        
        #get number 2
        while l2:
            
            number2+=str(l2.val)
            l2=l2.next
        
        #reverse the number and change to intiger
        number1=int(number1[::-1])
        number2=int(number2[::-1])
        
        #adding the numbers, reverse and 
        sum1=number1+number2
        sum1=str(sum1)
        sum1=sum1[::-1]
       
        # add the result to new list
        new_node=ListNode()
        head3=new_node
        for num in sum1:
            
            new=ListNode()
            new.val=num
            new_node.next=new
            new_node=new_node.next
            
        return head3.next
            
            
            
        
        