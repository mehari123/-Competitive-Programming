# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        head = lists
        
        for list1 in lists:
            
            node = list1
            while node:
                
                
                heappush(heap,node.val)
                
                node = node.next
        

        ans = ListNode()
        head = ans
        for h in range(len(heap)):
            
            ans.next = ListNode(heappop(heap))
            ans = ans.next
        
        return head.next