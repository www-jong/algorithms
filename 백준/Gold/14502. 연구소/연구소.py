from collections import deque
import copy
dx=[0,0,1,-1]
dy=[1,-1,0,0]
count_list=0
def bfs():
    graph_2=copy.deepcopy(graph)
    global count_list
    count=0
    for aa in range(1,n+1):
        for bb in range(1,m+1):
            if graph_2[aa][bb]==2:
                q=deque()
                q.append((aa,bb))
            else:continue
            while q:
                x,y=q.popleft()
                for i in range(4):
                    sx=x+dx[i]
                    sy=y+dy[i]
                    if 0<sx<=n and 0<sy<=m:
                        if graph_2[sx][sy]==0:
                            graph_2[sx][sy]=2
                            q.append((sx,sy))
                    
    for ss in range(1,n+1):
        for bb in range(1,m+1):
            if graph_2[ss][bb]==0:
                count+=1
    if count>count_list:
        count_list=count

def wellmake(con):
    global well
    if con==3:
        bfs()
        return
    for a in range(1,n+1):
        for b in range(1,m+1):
            if graph[a][b]==0:
                graph[a][b]=1
                wellmake(con+1)
                graph[a][b]=0
n,m=map(int,input().split())
graph=[[0]*(m+1)]
for i in range(n):
    graph.append([0]+list(map(int,input().split())))
well=[]
we=set()

wellmake(0)



print(count_list)
