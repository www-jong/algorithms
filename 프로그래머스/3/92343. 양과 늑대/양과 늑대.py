def solution(info, edges):
    res=0
    def func(x,a,b,y):
        nonlocal res
        if info[x]==0:
            a+=1
        else:
            b+=1
        if a<=b:
            return
        res=max(res,a)
        for i in y+tree[x]:
            func(i,a,b,[j for j in y+tree[x] if i!=j])
        
    tree=[[] for _ in range(len(info)+1)]
    for a,b in edges:
        tree[a].append(b)
    print(tree)
    func(0,0,0,[])
    
    return res