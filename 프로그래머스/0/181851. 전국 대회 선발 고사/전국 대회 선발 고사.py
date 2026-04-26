def solution(rank, attendance):
    tmp=sorted([(rank[i],i) for i in range(len(rank)) if attendance[i]],key=lambda x:x[0])[:3]
    answer=tmp[0][1]*10000+tmp[1][1]*100+tmp[2][1]
    return answer