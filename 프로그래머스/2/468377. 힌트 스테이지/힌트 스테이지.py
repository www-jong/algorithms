def solution(cost, hint):
    answer = float('inf')
    N=len(cost)

    for i in range(1<<(N-1)):
        tmp=0
        cnt=[0]*N

        for j in range(N):

            tmp+=cost[j][min(cnt[j],len(cost[j])-1)]
            if j<N-1 and (i&(1<<j)):
                price,*target=hint[j]
                tmp+=price
                for k in target:
                    if k-1<N:
                        cnt[k-1]+=1
        answer=min(tmp,answer)
    return answer