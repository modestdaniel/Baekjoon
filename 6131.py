import sys
n=int(sys.stdin.readline())
cnt=0
for i in range(1,501):
    for j in range(1,501):
        if pow(j,2)+n==pow(i,2): cnt+=1
print(cnt)