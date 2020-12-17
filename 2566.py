import sys
anstmp=[]
ans=[]
for i in range(9):
    tmp=list(map(int, sys.stdin.readline().split()))
    tmpMax=max(tmp)
    for j in range(9):
        if tmp[j]==tmpMax: anstmp.append( (i+1,j+1));  ans.append(tmpMax)

finalMax=max( ans)
for i in range(9):
    if finalMax==ans[i]:
        print(finalMax)
        print("%d %d"%(anstmp[i][0],anstmp[i][1] ))
        break