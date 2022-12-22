# Enter your code here. Read input from STDIN. Print output to STDOUT
members=int(input())
rooms={}
room_num=2
array=list(input().split())
size=len(array)
i=0

while i<size:
    if array[i] not in rooms:
        rooms[array[i]]=1
    else:
        rooms[array[i]]+=1
    i+=1
captain=0
family=0
for  key in rooms.keys():
    if rooms[key]==1:
        print( key)
    
