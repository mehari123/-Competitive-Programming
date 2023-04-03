n,k = map(int,input().split())

stack = []
org = k
nums = bin(n)[2:]
index = 0
for i in range(len(nums)-1,-1,-1):
    
    if nums[i] == "1":
        
        stack.append(2 ** index)
     
    index += 1 
    
k = k - len(stack)
stack2 = []   
while stack and  k > 0:
    
    if stack[-1] >= 2 :
        
        number = stack[-1] // 2
        stack.pop()
        stack.append(number)
        stack.append(number)
        k -= 1
    else:
        
        stack2.append(stack.pop())
        
stack.extend(stack2)
stack.sort()

if k == 0 and org == len(stack):
    
    print("YES")
    print(" ".join(str(s) for s in stack))
    
else:
    print("NO")
        
        
    
    
    

