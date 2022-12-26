class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        size=len(points)
        inf=float('inf')
        valid={}
        valid[inf]=-1
        for index,point in enumerate(points):
            if point[0]==x or point[1]==y:
                manthan_dist=abs((x-point[0])+(y-point[1]))
                if manthan_dist<list(valid.keys())[0]:
                    valid.pop(list(valid.keys())[0])
                    valid[manthan_dist]=index
        return list(valid.values())[0]
