def solution(n, costs):
    answer = 0
    nodes=[i for i in range(n+1)]
    weight=0
    def find(a):
        if a!=nodes[a]:
            nodes[a]=find(nodes[a])
        return nodes[a]

    def union(a,b):
        a=find(a)
        b=find(b)
        if a!=b:
            if a<b:
                nodes[b]=a
            else:
                nodes[a]=b

    costs.sort(key=lambda x:x[2])
    for a,b,c in costs:
        if find(a)!=find(b):
            weight+=c
            union(a,b)
    return weight