a=list(0 for i in range(0,42))
ans=0
for i in range(10):
    a[int(input())%42]+=1
for i in a:
    if i>0:
        ans+=1
print(ans)