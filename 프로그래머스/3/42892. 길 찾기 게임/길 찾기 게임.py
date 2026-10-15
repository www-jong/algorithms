def solution(nodeinfo):
    answer = [[]]
    N=len(nodeinfo)
    nodes=[(nodeinfo[i][0],nodeinfo[i][1],i+1) for i in range(N)]
    nodes.sort(key=lambda x:(-x[1],x[0]))
    le=[0]*(N+1)
    ri=[0]*(N+1)
    d={}
    for x,y,i in nodes:
        d[i]=x
        
    root=nodes[0][2]
    for x,y,i in nodes[1:]:
        now=root
        while True:
            if x<d[now]:
                if le[now]==0:
                    le[now]=i
                    break
                now=le[now]
            else:
                if ri[now]==0:
                    ri[now]=i
                    break
                now=ri[now]
    print(nodes)
    preorder=[]
    stk=[root]
    while stk:
        now=stk.pop()
        preorder.append(now)
        if ri[now]:
            stk.append(ri[now])
        if le[now]:
            stk.append(le[now])
    postorder=[]
    stk=[(root,0)]
    while stk:
        now,visit=stk.pop()
        if visit:
            postorder.append(now)
            continue
        stk.append((now,1))
        if ri[now]:
            stk.append((ri[now],0))
        if le[now]:
            stk.append((le[now],0))
    return [preorder,postorder]