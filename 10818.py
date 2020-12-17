N=int(input())
a=list(map(int,input().split()))

a.sort()
print("%d %d"%(a[0],a[-1]))