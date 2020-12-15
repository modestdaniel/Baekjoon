import sys
n=int(sys.stdin.readline())
tmp=[5]
for i in range(1,n):
    tmp.append(3*(i+1)+1)
#print(tmp)
print( sum(tmp)%45678)