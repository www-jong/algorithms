def solution(nodes, edges):
    def find(a):
        if parents[a]!=a:
            parents[a]=find(parents[a])
        return parents[a]

    def union(a,b):
        a=find(a)
        b=find(b)
        if a!=b:
            if a<b:
                parents[b]=a
            else:
                parents[a]=b

    answer = [0,0]
    parents={i:i for i in nodes}
    d={i:0 for i in nodes}
    for a,b in edges:
        union(a,b)
        d[a]+=1
        d[b]+=1

    groups={}
    for i in parents:
        if find(i) in groups:
            groups[find(i)].append(i)
        else:
            groups[find(i)] = [i]
    for group in groups.values():
        a,b=0,0
        for i in group:
            if i%2==d[i]%2:
                a+=1
            else:
                b+=1
        if a==1:
            answer[0]+=1
        if b==1:
            answer[1]+=1
    return answer
