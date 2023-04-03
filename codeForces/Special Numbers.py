test = int(input())

for t in range(test):
    
    n,k = map(int,input().split())
    num1 = 0
    i = 0
    while k > 0:
        
        if k&1:
            
            num1 += n**i
        k = k>>1
        i +=1
    print(num1 % (10 ** 9+ 7))
