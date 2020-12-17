import sys
def sh(n,m):
    cnt=0
    for a in range(1,n):
        for b in range(a+1,n):
            if (a**2+b**2+m)%(a*b)==0: cnt+=1
    return cnt
for _ in range(int(sys.stdin.readline())):
    n,m=map(int,sys.stdin.readline().split())
    print(sh(n,m ))