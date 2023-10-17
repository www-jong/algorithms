#트리의 부모 찾기 - 그래프이론


'''
2번부터 n번까지의 부모노드를 찾아라
1은 부모노드가 없다
'''
from sys import stdin

def DFS(gra,x,visit):
    stack = []
    visit[x] = True
    stack.append(x)
    while stack:
        node = stack.pop()
        for i in range(1,n+1):
            if gra[node][i]==1 and visit[i] == False:
                stack.append(i)
                visit[i] = True
                par[i] = node
def dfs2(gra,x,visit):
    stack=[]
    visit[x]=True
    stack.append(x)
    while stack:
        node=stack.pop()
        for i in gra[node]:
            if visit[i]==False and par[i]==0:
                stack.append(i)
                visit[i]=True
                par[i]=node
    

n = int( stdin.readline().rstrip())
gra = [[] for _ in range(n+1)]
par = [0] * (n+1)
visit = [False] * (n+1)

for _ in range(n-1):
    a,b = map(int, stdin.readline().rstrip().split())
    gra[a].append(b)
    gra[b].append(a)

dfs2(gra,1,visit)

for q in range(2,n+1):
    print(par[q])
