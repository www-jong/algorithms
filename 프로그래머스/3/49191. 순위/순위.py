def solution(n, results):
    answer = 0

    def get_depth(idx,flag=1):
        if visit[idx]:
            return set()
        visit[idx]=1
        tmp=set()
        for i in depth[idx][flag]:
            tmp.add(i)
            tmp=tmp.union(get_depth(i,flag))
        return tmp

    depth=[[set(),set()] for _ in range(n+1)]
    for a,b in results:
        depth[a][1].add(b)
        depth[b][0].add(a)
    n_depth=[[] for _ in range(n+1)]
    for i in range(1,n+1):
        visit=[0]*(n+1)
        parent=get_depth(i,0)
        visit=[0]*(n+1)
        child=get_depth(i,1)
        if len(parent)+len(child)==n-1:
            answer+=1
    return answer