# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
       
            
            
       
        
        if list1==None:
            return list2
        elif list2==None:
            return list1
        
        if list1.val<=list2.val:
            head=list1
        else:
            head=list2
            
        head2=list2
        dummy=head
        new_node=ListNode()
        last="0"
        
        while list1 and list2:
            if list1.val<=list2.val:
                
                new_node.next=list1
                new_node=new_node.next
                list1=list1.next
                last="1"
            else:
                new_node.next=list2
                new_node=new_node.next
                list2=list2.next
                last="2"
                
        if last=="1":
            new_node.next=list2
        else:
            new_node.next=list1
        return head
    
            
#         while list2:
            
#             if list1.val>=list2.val:
                
#                 list1.next,list2.next,list2=list2,list1.next,list2.next
#                 list1=list1.next.next
#                 print("if")
#                 print(list1)
#                 print(head)
                
#             elif list1.val>list2.val:
                
#                 list1.next,list2.next,list2=list2,list1.next,list2.next
#                 # list1=list1.next
#                 print("elf")
#                 print(list1)
#                 print(list2)
#             else:
#             #     # list2.next,list1.next,list1=list1,list2.next,list1.next
#                 list1.next=list1
#             #     print("else")
#             #     print(list1)
                
#         return head
                
            
                
                
                
                
        