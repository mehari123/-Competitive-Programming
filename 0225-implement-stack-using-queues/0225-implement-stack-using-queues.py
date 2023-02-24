class MyStack:

    def __init__(self):
        
        self.list1=[]
    def push(self, x: int) -> None:
        
        self.list1.append(x)
        

    def pop(self) -> int:
        
        return self.list1.pop()
        
    def top(self) -> int:
        
        return self.list1[-1]

    def empty(self) -> bool:
        
        if not self.list1:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()