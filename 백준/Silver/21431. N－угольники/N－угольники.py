N,K=map(int,input().split())
res=[1]*(N-1)
while True:
    now=sum(res[1-N:])
    if now>K:
        break
    res.append(now)
print(len(res))
print(*res)