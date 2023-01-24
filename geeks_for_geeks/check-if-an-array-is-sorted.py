#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        for index in range(1,len(arr)):
            
            if arr[index-1]>arr[index]:
                return 0
        return 1
