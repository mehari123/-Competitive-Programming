test = int(input())

for t in range(test):
    
    n = int(input())
    array = list(map(int,input().split()))
    ans = 0
    count_bit = [0]* 64
    
    for arr in array:
        
        count_bit[arr.bit_length()] += 1

    
    for count1 in count_bit:
        
        ans +=(count1 * (count1 -1))//2
    print(ans)
