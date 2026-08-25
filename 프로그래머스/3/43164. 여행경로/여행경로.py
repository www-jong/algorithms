def solution(tickets):
    check=set()

    graph=[[]]
    d={'ICN':0}
    d_r={0:'ICN'}
    check.add('ICN')
    idx=0
    for a,b in tickets:
        if a not in check:
            check.add(a)
            idx+=1
            d[a]=idx
            d_r[idx]=a
            graph.append([])

        if b not in check:
            check.add(b)
            idx+=1
            d[b]=idx
            d_r[idx]=b
            graph.append([])

        graph[d[a]].append(d[b])
    N=len(graph)

    for i in range(N):
        graph[i].sort(key=lambda x:d_r[x],reverse=True)

    in_deg=[0]*N
    out_deg=[0]*N
    for a,b in tickets:
        in_deg[d[b]]+=1
        out_deg[d[a]]+=1

    path=[]
    answer=[]
    def func(now):
        while graph[now]:
            next=graph[now].pop()
            func(next)
        path.append(now)
    func(0)
    for i in path[::-1]:
        answer.append(d_r[i])

    return answer