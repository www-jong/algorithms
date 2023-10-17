from collections import deque
n=int(input())
graph_1=[[0]*(n+1)]
graph_2=[[0]*(n+1)]
visit_1=[[0]*(n+1) for i in range(n+1)]
visit_2=[[0]*(n+1) for i in range(n+1)]

for i in range(n):
    a=input()
    a_1=a.replace("R","G")
    graph_1.append(["0"]+list(a))
    graph_2.append(["0"]+list(a_1))
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def bfs(graph,visit):
    count=0
    for aa in range(1,n+1):
        for bb in range(1,n+1):
            if visit[aa][bb]==0:
                count+=1
                q=deque()
                q.append((aa,bb))
                ch=graph[aa][bb]
                visit[aa][bb]=1
            else:continue
            while q:
                x,y=q.popleft()
                for i in range(4):
                    sx=x+dx[i]
                    sy=y+dy[i]
                    if 1<=sx<=n and 1<=sy<=n:
                        if graph[sx][sy]==ch and visit[sx][sy]==0:
                            q.append((sx,sy))
                            visit[sx][sy]=1
    return count
print("%d %d"%(bfs(graph_1,visit_1),bfs(graph_2,visit_2)))

                            
                    
    