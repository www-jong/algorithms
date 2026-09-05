def solution(s):
    answer = 1
    N=len(s)
    dp=[[0]*N for _ in range(N)]
    for i in range(N):
        dp[i][i]=1
    for i in range(N-1):
        if s[i]==s[i+1]:
            dp[i][i+1]=1
            answer=2
            
    for i in range(3,N+1):
        for st in range(N-i+1):
            end=st+i-1
            if s[st]==s[end]  and dp[st+1][end-1]==1:
                dp[st][end]=1
                answer=max(answer,i)
    return answer