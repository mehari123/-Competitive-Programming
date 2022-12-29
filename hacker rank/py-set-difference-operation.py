# Enter your code here. Read input from STDIN. Print output to STDOUT
size_eng=int(input())
eng_stu=[]
eng_stu=list(input().split())
size_french=int(input())
french_stu=set()
french_stu=list(input().split())
english_only=0
for i in eng_stu:
    if i in french_stu:
        continue
    else:
        english_only+=1
        
print(english_only)
