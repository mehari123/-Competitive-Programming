# Enter your code here. Read input from STDIN. Print output to STDOUT
size=int(input())
set1=set(input().split())
size2=int(input())
set2=set(input().split())
print(len(set.union(set1,set2)))
