mylist=[]
a,b= map ( int, input().split())
for i in range(1,a+1):
   if a%i==0: mylist.append(i)
if b>len(mylist): print(0)
else : print(mylist[b-1])