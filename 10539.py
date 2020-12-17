import sys
n=int(sys.stdin.readline())
b=list(map(int,sys.stdin.readline().split()))
a=[b[0]]

for i in range(1,n):
    a.append( (i+1)*b[i]-sum(a[:i]) )

for _ in range(n):
    print(a[_], end=' ')