from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):

        self.heap = list()
        self.sorted1 = SortedList()
        
    def addNum(self, num: int) -> None:
        
        self.sorted1.add(num)
        heappush(self.heap,num)

    def findMedian(self) -> float:

        sizee = len(self.sorted1)

        if sizee % 2 != 0:

            return self.sorted1[sizee//2]

        else:

            mid = self.sorted1[sizee//2] + self.sorted1[(sizee//2) -1] 
            return mid / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()