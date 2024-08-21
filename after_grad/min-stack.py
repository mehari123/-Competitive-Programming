class MinStack:

    def __init__(self):

        self.num_dict = defaultdict(int)
        self.heap = []
        self.stack = []

    def push(self, val: int) -> None:

        self.stack.append(val)
        heapq.heappush(self.heap,val)
        self.num_dict[val] += 1

    def pop(self) -> None:

        val = self.stack.pop()
        self.num_dict[val] -= 1
        val1 = self.heap[0]
        if val1 == val:

            val1 = heapq.heappop(self.heap)

    def top(self) -> int:

        return self.stack[-1]
        
    def getMin(self) -> int:

        val = self.heap[0]
        while self.num_dict[val] <= 0:

            heapq.heappop(self.heap)
            val = self.heap[0]

        return val

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()