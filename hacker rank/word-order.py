# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
words={}
for i in range(n):
    word=input()
    if word in words:
        words[word]+=1
    else:
        words[word]=1
print (len(words))
for key in words:
    print (words[key],end=" ")
