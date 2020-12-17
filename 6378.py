import sys
sys.setrecursionlimit(10**6)
def digitalroot(n):
    return sum(map(int,n)) if len(n) ==1 else digitalroot(str(sum(map(int,n))))

while True:
    n=input()
    if n=='0': exit()
    else :
        print (digitalroot(n))