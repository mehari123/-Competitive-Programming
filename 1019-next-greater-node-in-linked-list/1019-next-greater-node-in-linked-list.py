# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        stack=[]
        ans=[]
        index=0
        
        while head:
            
            # compare the current head value to the previous values on the stack 
            while stack and stack[-1][1]<head.val:
                
                #getting the index using "stack.pop()[0]" and assign head value
                ans[stack.pop()[0]]=head.val
            
            #stor index and the value for future (will may find greater element)
            stack.append([index,head.val])
            
            # append 0 until greater vallue is found
            ans.append(0)
            index+=1
            head=head.next
            
        return ans
            
                
                
                
        