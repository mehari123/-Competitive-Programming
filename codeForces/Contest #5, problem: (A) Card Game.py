size1=int(input())
array=[]
array=list(map(int,input().split()))
wube=0
ibsa=0
left=0
right=len(array)-1
for index,num in enumerate(array):
    max1=0
    maxi1=max(array[left],array[right])
    if index%2==0:
        if maxi1==array[left]:
            wube+=maxi1
            left+=1
        elif maxi1==array[right]:
            wube+=maxi1
            right-=1
    else:
        if maxi1==array[left]:
            ibsa+=maxi1
            left+=1
        elif maxi1==array[right]:
            ibsa+=maxi1
            right-=1
print(wube,ibsa)
        
