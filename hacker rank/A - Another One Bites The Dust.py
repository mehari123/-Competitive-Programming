chars=list(map(int,input().split()))
str1=int(chars[0])
str2=int(chars[1])
str3=int(chars[2])

if str1>str2:
  print(str2+str2+1+(str3*2))
elif str1==str2:
   print(str1+str2+(str3*2))
else:
   print(str1+str1+1+(str3*2))
