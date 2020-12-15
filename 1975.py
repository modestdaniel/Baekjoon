import sys
t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    cnt = 0

    for j in range(2, n+1):
        tmp = n
        while (tmp//j)!=0:
            if tmp%j==0:
                cnt+=1
                tmp/=j
            else: break
    print(cnt)