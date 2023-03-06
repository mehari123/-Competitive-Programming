testCase = int(input())

for test in range( testCase ):
    
    n, m = map(int,input().split())
    high = min(n,m)
    lowt = 0
    orginal = (n + m) //4
    
    while lowt < high:
        
        mid = (high+lowt)//2
        
        if mid >= orginal:
            
            high = mid
            
        else:
            
            lowt = mid + 1
    
    print(high)
