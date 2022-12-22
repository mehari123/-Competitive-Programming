 Enter your code here. Read input from STDIN. Print output to STDOUT
test_case=int(input())
for i in range(test_case):
    cube_num="case"+str(i)
    globals()[cube_num]=int(input())
    cubes="cube"+str(i)
    globals()[cubes]=list(map(int,input().split()))
 
name="cube0"
globals()[name]
# print(test_case)
print(globals()[name][0])
# print(cube0)
    
for i in range(test_case):
    cube_num="case"+ str(i)
    cubes="cube"+str(i)
    k=0
    i=globals()[cubes][0]
    j=globals()[cubes][globals()[cube_num]-1]
    while k<len(globals()[cubes]):
        if i>=globals()[cubes][k]:
            i=globals()[cubes][k]
            globals()[cubes].pop(k)
        elif j>=globals()[cubes][globals()[cube_num]-k]:
            j=globals()[cubes][globals()[cube_num]-k]
            globals()[cubes].pop(globals()[cube_num]-k)
    if globals()[cubes]==[]:
        print("Yes")
    else:
        print ("no")
