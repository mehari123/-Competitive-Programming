def accept_block():
    size=int(input())
    block=list(map(int,input().split()))
    return size,block

test_case=int(input())
for test in range(test_case):
    size,block=accept_block()
    left_pointer=0
    right_pointer=size-1
    stacked='Yes'

    if block[right_pointer]>=block[left_pointer]:
        top_block=block[right_pointer]
    else:
        top_block=block[left_pointer]
    
    while left_pointer<=right_pointer:
        if block[left_pointer]>=block[right_pointer] and top_block>=block[left_pointer]:
             top_block=block[left_pointer]
             left_pointer+=1
        elif block[left_pointer]<=block[right_pointer] and top_block>=block[right_pointer]:
            top_block=block[right_pointer]
            right_pointer-=1
        else:
            stacked="No" 
            break  
    print(stacked)
