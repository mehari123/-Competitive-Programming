input_size=int(input())
 
for Tshirt in range(input_size):
    tshirt1,tshirt2=input().split()
    x_len1=len(tshirt1)-1
    x_len2=len(tshirt2)-1
    
    if tshirt1[x_len1]==tshirt2[x_len2]:
        
        if x_len1==x_len2:
            print("=")
        elif tshirt1[x_len1]=="S":
            if x_len1>x_len2:
                print("<")
            else:
                print(">")
        elif x_len1>x_len2:
            print(">")
        else:
            print("<")
            
    elif tshirt1[x_len1]=="L" and tshirt2[x_len2]=="M":
        print(">")
    elif tshirt1[x_len1]=="L" and tshirt2[x_len2]=="S":
        print(">")
    elif tshirt1[x_len1]=="M" and tshirt2[x_len2]=="S":
        print(">")
    else:
        print("<")
