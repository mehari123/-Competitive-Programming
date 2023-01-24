size1,size2=map(int,input().split())

arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))

arr3=[0]*(size1+size2)

pointer1=0
pointer2=0
index=0
while index<len(arr3):
    
    
    if pointer1==size1:
        
        arr3[index]=arr2[pointer2]
        pointer2+=1
    elif pointer2==size2:
        
        arr3[index]=arr1[pointer1]
        pointer1+=1
        
    
    elif arr1[pointer1]<=arr2[pointer2]:
        
        arr3[index]=arr1[pointer1]
        pointer1+=1
    else:
        arr3[index]=arr2[pointer2]
        
        pointer2+=1
    index+=1
    
index=0
while index<len(arr3):
    print(arr3[index],end=" ")
    index+=1
