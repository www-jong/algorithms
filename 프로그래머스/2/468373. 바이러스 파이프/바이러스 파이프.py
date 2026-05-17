def solution(n, infection, edges, k):
    def func(x,visit,c):
        nonlocal res
        if x==k:
            res=max(res,len(visit))
            return
        for i in range(3):
            if c==i:
                continue
            t_visit=set()
            li=list(visit)
            while li:
                now=li.pop()
                for j in graph[now][i]:
                    if j not in visit and j not in t_visit:
                        t_visit.add(j)
                        li.append(j)
            func(x+1,visit.union(t_visit),i)

    graph=[[[] for _ in range(3)] for _ in range(n+1)]
    res=0
    for a,b,c in edges:
        graph[a][c-1].append(b)
        graph[b][c-1].append(a)
    func(0,{infection},-1)
    return res