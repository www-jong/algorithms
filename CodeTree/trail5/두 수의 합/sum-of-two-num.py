n, k = map(int, input().split())
arr = list(map(int, input().split()))
d={}
res=0

for i in arr:
    res+=d.get(k-i,0)
    d[i]=d.get(i,0)+1

print(res)