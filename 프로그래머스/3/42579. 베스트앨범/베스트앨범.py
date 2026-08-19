def solution(genres, plays):
    d={}
    g={}
    N=len(genres)
    answer = []
    for i in range(N):
        if genres[i] in d:
            d[genres[i]].append((i,plays[i]))
            g[genres[i]]+=plays[i]
        else:
            d[genres[i]]=[(i,plays[i])]
            g[genres[i]]=plays[i]
    tmp=[(k,v) for k,v in g.items()]
    tmp.sort(key=lambda x:-x[1])
    for i,_ in tmp:
        now=sorted(d[i],key=lambda x:-x[1])          
        for k,v in now[:2]:
            answer.append(k)
    return answer