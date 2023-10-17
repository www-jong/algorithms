import math
def g(li):
    gc=0
    for i in range(len(li)-1):
        for j in range(i+1,len(li)):
            gc+=(math.gcd(li[i],li[j]))
    return gc

t=int(input())
for i in range(t):
    a=list(map(int,input().split()))[1:]
    print(g(a))