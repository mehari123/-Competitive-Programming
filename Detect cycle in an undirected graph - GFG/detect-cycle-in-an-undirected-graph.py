from typing import List
# class Solution:
#     #Function to detect cycle in an undirected graph.
# 	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
# 		#Code here
# 		color = [0] * V
# 		def Cycle(node,parent):
		    
# 		    if color[node] == 2:
		        
# 		        return True
		        
# 		    if color[node] == 0:
		        
# 		        color[node] = 1
		        
# 		    for li in adj[node]:
		        
# 		        if li != parent:
		            
#     		        if color[li] == 0:
    		            
#     		            if not Cycle(li,node):
    		                
#     		                return False
    		                
#     		color[node] = 2
#     		return True
    		        
# 		for i in range(V):
		   
# 		    if color[i] == 0:
		        
# 		        if not Cycle(i,None):
		            
# 		            return 1
		    
# 	    return 0
	    
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    
		color = [0] * V
		def dfs(node, parent):
		    
		    if color[node] == 2:
		        
		        return True
		    
		    if color[node] == 0:
		        
    		    color[node] = 1
    		    for li in adj[node]:
    		        
    		        if li != parent:
    		            
    		            if not dfs(li,node):
    		                
    		                return False
        		            
    		    color[node] = 2
    		    return True
    		    
    	    return False
	    
	    for i in range(V):
	        
	        if color[i] == 0:
	            
	            if not dfs(i,None):
	                
	                return 1
	                
	    return 0
		
    

#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends