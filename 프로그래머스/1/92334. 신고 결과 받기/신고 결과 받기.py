def solution(id_list, report, k):
    answer = [0]*len(id_list)
    id={j:i for i,j in enumerate(id_list)}
    d={}
    s=set()
    for i,j in enumerate(report):
        a,b=j.split()
        if b not in d:
            d[b]={a}
        else:
            d[b].add(a)
        if len(d[b])==k:
            s.add(b)
    for i in s:
        for j in d[i]:
            answer[id[j]]+=1
    return answer