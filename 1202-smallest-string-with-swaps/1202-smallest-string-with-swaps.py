class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[px] = py
            self.rank[py] += 1

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        n = len(s)
        uf = UnionFind(n)
        character = defaultdict(list)
        
        for ch1,ch2 in pairs:
            uf.union(ch1, ch2)
        
        for i in range(n):
            character[uf.find(i)].append(s[i])
        
        for root in character:
            character[root].sort(reverse=True)
        
        ans = ""
        for i in range(n):
            ans += character[uf.find(i)].pop()
            
        return ans
