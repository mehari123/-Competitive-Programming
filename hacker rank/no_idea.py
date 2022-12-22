# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m= map(int, input().split())
given_num=list(map(int, input().split()))
like=set(map(int, input().split()))
unlike=set(map(int, input().split()))

print(sum([(i in like)-(i in unlike) for i in given_num]))
