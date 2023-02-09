# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        odd, p= head, head and head.next 
        
        while p and p.next:
            odd.next, p.next.next, p.next = p.next, odd.next, p.next.next #insert 
            odd, p = odd.next, p.next 
        return head

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         even=head
#         odd=None
#         dummy=head
#         count1=0
#         # even1=None
#         while dummy.next:
            
#             brek=False
#             count1+=1
#             dummy=even
#             odd=ListNode()
#             index=0
#             while index<count1 and dummy:
#                 odd=dummy.next
#                 temp_node=odd.next
#                 odd.next=None
#                 index+=1
#                 dummy=temp_node
#                 if not temp_node:
#                     brek=True
#                     break
                    
#             # if brek:
#             #     break
#             even.next=dummy
#             even=even.next
#             even1=even
#             if even:
#                 temp_node=even.next
#                 even.next=odd
#                 even=even.next
#                 even.next=temp_node
#             else:
#                 break
#             even=even1
            
#         # even.next=odd
#         print(head)
#         print(even)
#         print(odd)
            