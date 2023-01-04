# Enter your code here. Read input from STDIN. Print output to STDOUT
superSet=set(input().split())
numSubSet=int(input())
isSuper="True"
for numSet in range(numSubSet):
    subSet=set(input().split())
    if not superSet.issuperset(subSet):
        isSuper="False"
        break
print(isSuper)
