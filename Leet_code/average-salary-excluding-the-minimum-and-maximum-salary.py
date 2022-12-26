class Solution:
    def average(self, salary: List[int]) -> float:
        sorted_sal=sorted(salary,reverse=False)
        size=len(sorted_sal)
        sorted_sal.pop(0)
        sorted_sal.pop(size-2)
        avg=sum(sorted_sal)/(len(sorted_sal))
        return avg
