test = int(input())

for t in range(test):
    
    num = int(input())
    binary = bin(num)
    bi_str = str(binary)
    bi_str = bi_str[2:]
    bi_str2 = bi_str[::-1]
    index = 0
    ans = []
    found = False
    and_f = 0
    
    while index < len(bi_str2):
        
        if bi_str2[index] == "1" and (not found):
        
            ans.append(1)
            and_f = index
            found = True
            index += 1
            
        elif found or bi_str2[index] == "0" :
            
            ans.append(0)
            index += 1
    
    x_or = len(bi_str2)-1
    found = False
    
    while x_or > and_f and (not found):
            
        if bi_str2[x_or] == "1":
            
            found = True
            break
            
        x_or -= 1
      
    if (not found )and x_or > 0:
        
        ans[0] = 1
        
    elif not found and x_or == 0:
        
        ans.append(1)
    
    ans_r = ans [::-1]
    res = int("".join(str(i) for i in ans_r),2)
    print(res)

        
