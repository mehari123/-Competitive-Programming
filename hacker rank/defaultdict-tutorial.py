# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
defdict = defaultdict(list)
n, m =  map(int, input().split())
groupA, groupB = [], []
for i in range(n):
    temp = input()
    defdict[temp].append(i+1)

for j in range(m):
    groupB.append(input())

for let in groupB:
    if let in defdict:
        print(" ".join(map(str, defdict[let])))
    else:
        print(-1)

# m,n=map(int,input().split())
# A=[]
# B=[]
# for i in range(m):
#     A.append(input())
# for i in range(n):
#     B.append(input())
# def def_value():
#     return "-1"
      
# dict1=defaultdict(def_value)
# for char in B:
#     for index,char2 in enumerate(A):
#         if char==char2:
#             if dict1[char]=="-1":
#                 dict1[char]=[]
#             dict1[char].append(str(index+1))
# for i in B:
#     print(" ".join(dict1[i]))
