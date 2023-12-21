N=int(input())
li=[]
for i in range(N):
    li.append(list(map(int,input().split())))
dp={}

def dfs(now,visited):
    if visited==(1<<N)-1:
        if li[now][0]:
            return li[now][0]
        else:
            return int(1e9)
    if (now,visited) in dp:
        return dp[(now,visited)]
    min_cost=1e9
    for next in range(1,N):
        if li[now][next]==0 or visited&(1<<next):
            continue
        cost=dfs(next,visited|(1<<next))+li[now][next]
        min_cost=min(min_cost,cost)
    dp[(now,visited)]=min_cost
    return min_cost
print(dfs(0,1))