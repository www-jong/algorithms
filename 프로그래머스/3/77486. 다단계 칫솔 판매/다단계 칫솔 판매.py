def solution(enroll, referral, seller, amount):
    def func(idx,v):
        if idx==0:
            return
        answer[idx]+=v-v//10
        if v//10>=1:
            func(parent[idx],v//10)

    N,M=len(enroll)+1,len(seller)
    answer = [0]*(N)
    parent=[i for i in range(N)]
    d={}
    d["민호"]=0
    idx=1
    for i in enroll:
        d[i]=idx
        idx+=1
    for i in range(1,N):
        now=referral[i-1]
        if now=='-':
            parent[i]=0
        else:
            parent[i]=d[now]
    for i in range(M):
        v=100*amount[i]
        answer[d[seller[i]]]+=v-v//10
        func(parent[d[seller[i]]],v//10)
    return answer[1:]