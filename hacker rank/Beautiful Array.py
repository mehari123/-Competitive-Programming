n=input()

array=list(map(int,input().split()))

set1=set()
set2=set()
set3=set()
   
nega1=0
nega2=1
negative1=1
negative2=2

for index,num in enumerate(array):
 
   
    if num<0 and len(set1)<1:
         set1.add(num)
         
    elif nega1<1 and num<0:
        negative1=num
        nega1=2
        nega2=0
    elif nega2<1 and num<0:
        negative2=num
        nega2=1
        set2.add(negative1)
        set2.add(negative2)
    elif num ==0 or (num<0 and len(set2)>1):
       
        set3.add(num)
        
   
    elif num>0 or negative2<0:
        set2.add(num)
    if index==len(array)-1 and negative2>0 and negative1<0:
            set3.add(negative1)
    
        

print(str(len(set1)),*set1)         
print(str(len(set2)),*set2)
print(str(len(set3)),*set3)
