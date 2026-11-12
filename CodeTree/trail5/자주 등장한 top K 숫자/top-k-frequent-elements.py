n, k = map(int, input().split())
arr = list(map(int, input().split()))
d={}
for i in arr:
    if i in d:
        d[i]+=1
    else:
        d[i]=1


s=sorted([(k,v) for k,v in d.items()],key=lambda x:(-x[1],-x[0]))

for i in range(k):
    print(s[i][0],end=" ")