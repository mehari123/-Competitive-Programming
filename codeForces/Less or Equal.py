n,k=map(int,input().split())

arra=list(map(int,input().split()))

arra.sort

arr_count={}

for num in arra:
    
    if num in arr_count:
        
        arr_count[num]+=1
    else:
        arr_count[num]=1
        
count1=[]
index=0
found=-1
sum1=0
arr_count=dict(sorted(arr_count.items(), key=lambda item: item[0]))
for key,value in arr_count.items():
    
    sum1+=value
    
    if k==0:
        if key==1:
            found=-1
        else:
            found=key-1
        break
    elif sum1==k:
       
       found=key
       break
    elif sum1>k:
        found=-1
        break
    
    index+=1

if k>=n:
    found=arr_count.popitem()
    found=found[0]
print(found)
