import sys
ans=0
tmp=[]
for i in range(10):
    a,b=map(int,sys.stdin.readline().split())
    ans=ans-a+b
    tmp.append(ans)
print(max(tmp))