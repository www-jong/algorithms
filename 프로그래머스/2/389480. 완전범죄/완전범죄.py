def solution(info, n, m):
    info.sort(key=lambda x:(x[0],-x[1]))
    dp=[float('inf')]*m
    dp[0]=0 # dp[j]= b의 흔적이 j일때 A가남긴 최소양
    
    for a,b in info:
        tmp=[float('inf')]*m
        for i in range(m-1,-1,-1):

            tmp[i]=min(tmp[i],dp[i]+a)
            if i+b<m:
                tmp[i+b]=min(tmp[i+b],dp[i])
        dp=tmp
    answer = min([i for i in dp if i<n],default=-1)
    return answer