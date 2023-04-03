test = int(input())

for t in range(test):
    
    num1 = int(input())
    
    array = list(map(int,input().split()))
    
    print(array[num1-1])
