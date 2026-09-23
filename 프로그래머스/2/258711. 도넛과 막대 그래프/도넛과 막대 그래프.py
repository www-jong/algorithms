from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)
def solution(edges):
    answer = [0,0,0,0]#정점,도넛,막대,8
    def func(idx):
        nonlocal flag
        if idx in tmp:
            flag=3
        for next in graph[idx]:
            if not visit[next]:
                visit[next]=1
                func(next)
            else:
                if flag!=3:
                    flag=1

    graph=defaultdict(set)
    check=[0]*1000001
    node=0
    tmp=set()
    N=0
    for a,b in edges:
        N=max(N,a,b)
        graph[a].add(b)
        if len(graph[a])>1:
            tmp.add(a)
        check[a]+=1
        check[b]-=1
    visit=[0]*(N+1)
    for k in tmp:
        if check[k]>0:
            node=k
            break
    answer[0]=node
    for i in graph[node]:
        flag=2
        func(i)
        answer[flag]+=1
    return answer