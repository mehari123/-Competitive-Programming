class Node():
    def __init__(self,val):
        self.val=val
        self.next=None
        
class MyLinkedList:
    

    def __init__(self):
        self.head=None

    def get(self, index: int) -> int:
        if not self.head:
            return -1
        current_node=self.head
        current=0
        while current_node:
            if current==index:
                return current_node.val
            current+=1
            current_node=current_node.next
        return -1
        
    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head=Node(val)
            return 
        new_node=Node(val)
        new_node.next=self.head
        self.head=new_node
          
    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head=Node(val)
            return 
        current_node=self.head
        while current_node.next:
            current_node=current_node.next
        new_node=Node(val)
        current_node.next=new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        if not self.head and index==0:
            self.addAtHead(val)
            return
        if not self.head:
            return 
        current_node=self.head
        current=0
        new_node=Node(val)
        if index==0:
            self.addAtHead(val)
            return 
        while current_node:
            if current==index-1: 
                new_node.next=current_node.next
                current_node.next=new_node
                return    
            current_node=current_node.next
            current+=1
        return 

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        current_node=self.head
        current=0
        if index==0:
            self.head=current_node.next
            return
        while current_node :
            if current==index-1 and current_node.next:
                current_node.next=current_node.next.next
            current_node= current_node.next
            current+=1
        return
        
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)