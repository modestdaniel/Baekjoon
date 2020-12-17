mylist=[]
for _ in range(7):
    n=int(input())
    if n%2==1: mylist.append(n)
if not mylist:print(-1)
else :
    print(sum(mylist))
    print (min(mylist))