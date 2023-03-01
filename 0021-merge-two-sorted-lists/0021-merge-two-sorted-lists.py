# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head1=list1
        head2=list2
        new_node=ListNode(0)
        head3=new_node
        last=0
        
        if list1==None:
            return list2
        elif list2==None:
            return list1
    
            
        def merge(list1,list2):
            
            nonlocal new_node
            nonlocal last
            if list1==None or list2==None:
                
                if last==1:
                    new_node.next=list2
                else:
                    new_node.next=list1
                    
                return new_node
            
            elif list1.val<=list2.val:
                
                temp=list1.next
                new_node.next=list1
                new_node=new_node.next
                new_node.next=None
                
                list1=temp
                # list1=list1.next
                last=1
                
            else:
                temp=list2.next
                new_node.next=list2
                
                new_node=new_node.next
                new_node.next=None
                
                list2=temp
                # list2=list2.next
                last=2
            print(list1,list2)
            return merge(list1,list2)
                
        merge(head1,head2)
        
        return head3.next
        
        
        
                
                
            
            
        
        
                
                
                
                
                
                
                
                
                
                
                
                
                
        
        
       
                
        
                
                
                
                
                
                
                
                
                
        