from collections import defaultdict 
n = int(input())
graph = []
for i in range(n):

    r = input().strip().split()
    graph.append(list(r))
    
indegree = defaultdict(lambda:0)
outdegree = defaultdict(lambda:0)
# print(graph)
index =0
for r_index,row in enumerate(graph):
    # print(index,r_index)
    index += 1
    # print(row)
    # print(len(row))
    for c_index,c in enumerate(row):
        # print(c_index,len(row),c)
        if c == "1":
            indegree[r_index +1] += 1
            outdegree[c_index +1] += 1
 
sources = []
all = {**outdegree,**indegree}

inboth = []

for i in range(1,len(graph) + 1):
    
    if i not in all:
        inboth.append(i)
        
# print(all)
for out in outdegree:  
     
    if out not in indegree:

        sources.append(out) 
        
sink = []
for ind in indegree:
    
    if ind not in outdegree:
        sink.append(ind)  
                
sink = sink +inboth
sources = sources +inboth
sink.sort()
sources.sort()
print(len(sink)," ".join([str(str1) for str1 in sink]))
print(len(sources)," ".join([str(str1) for str1 in sources]))